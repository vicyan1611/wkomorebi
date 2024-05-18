import pystray
from komorebic_client import WKomorebic
from PIL import Image
import logging

import win32pipe, win32file
import time
import json

BUFFER_SIZE = 1024 * 64

class WkomorebiTray:
    def __init__(self) -> None:
        self.komorebic = WKomorebic()
        self.is_running = True
        self.komorebic.start_komorebi()

        # init icon's images
        self.images = [None] * 10
        self.images[0] = Image.open('assets/p.png')
        for id in range(1, 10):
            image_path = f'assets/{id}.png'
            self.images[id] = Image.open(image_path)

        # init icon's menu
        self.menu = pystray.Menu(pystray.MenuItem('Exit Wkomorebi', self.exit_wkomorebi),
                                 pystray.MenuItem('Pause/Continue Wkomorebi', self.pause_wkomorebi))
        self.icon = pystray.Icon('wkomorebi', icon=self.images[0], menu=self.menu)

        # init komorebi listener
        self.pipe = None
        self.pipename = 'wkomorebi_listener'
        self.create_named_pipe()
        self.connect_komorebi()
        pass
        
    def create_named_pipe(self) -> None:
        self.pipe = win32pipe.CreateNamedPipe(f'\\\\.\\pipe\\{self.pipename}',
                                              win32pipe.PIPE_ACCESS_DUPLEX,
                                              win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
                                              1,
                                              BUFFER_SIZE,
                                              BUFFER_SIZE,
                                              50,
                                              None)
        logging.info(f'Created named pipe ${self.pipename}')
    
    def connect_komorebi(self) -> None:
        self.komorebic.subscribe_pipe(self.pipename)
        logging.info("connect successfully")

    def change_icon(self, workspace:int) -> None:
        self.icon.icon=self.images[workspace+1]
        pass
    
    def exit_wkomorebi(self) -> None:
        self.icon.stop()
        self.is_running = False
        win32pipe.DisconnectNamedPipe(self.pipe)
        win32file.CloseHandle(self.pipe)
        self.komorebic.stop_komorebi();
        return

    def pause_wkomorebi(self) -> None:
        self.komorebic.pause_komorebi()
        pass

    def run(self) -> None:
        self.icon.run_detached()
        
        # read komorebi event
        try:
            while self.is_running:
                buffer, bytes_to_read, status = win32pipe.PeekNamedPipe(self.pipe, 1);
                if not bytes_to_read:
                    time.sleep(0.1)
                    continue
                

                result, data = win32file.ReadFile(self.pipe, bytes_to_read)
                if not data.strip():
                    continue
                event = json.loads(data.decode("utf-8"))
                # event = json.loads(data)
                # print(json.dumps(event, indent=4))
                
                event_state = event['state']
                if not event_state['is_paused']:
                    num = int(event_state['monitors']['elements'][0]['workspaces']['focused'])
                    self.change_icon(num)
                else:
                    self.change_icon(-1)
                
        except (BaseException, Exception):
            win32pipe.DisconnectNamedPipe(self.pipe)
            win32file.CloseHandle(self.pipe)
            print("There are exceptions")
            
if __name__ == "__main__":
    wkomorebi = WkomorebiTray()
    wkomorebi.run()