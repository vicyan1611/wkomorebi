import win32pipe, win32file
import logging
import time
import json

from komorebic_client import WKomorebic
BUFFER_SIZE = 1024 * 64
class KomorebiListener:

    def __init__(self) -> None:
        self.pipename = 'wkomorebi'
        self.buffer_size = BUFFER_SIZE
        self.pipe = None
        self.komorebic = WKomorebic()
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
        logging.info(f'Created named pip ${self.pipename}')
        print("created namedpipe")

    def connect_komorebi(self) -> None:
        self.komorebic.subscribe_pipe(self.pipename)
        print("connect successfully")

    def read_komorebi_events(self) -> None:
        try:
            while True:
                buffer, bytes_to_read, status = win32pipe.PeekNamedPipe(self.pipe, 1);
                if not bytes_to_read:
                    time.sleep(0.1)
                    continue
                
                result, data = win32file.ReadFile(self.pipe, bytes_to_read)
                if not data.strip():
                    continue
                
                event = json.loads(data.decode("utf-8"))
                event_name = event['event']['type']
                event_state = event['event']['state']
                if event_name and event_state:
                    print(event_name)   
                # break
        except (BaseException, Exception):
            win32file.CloseHandle(self.pipe)
            # print(Exception)
if __name__ == "__main__":
    tko = KomorebiListener()
    tko.create_named_pipe()
    tko.connect_komorebi()
    tko.read_komorebi_events()