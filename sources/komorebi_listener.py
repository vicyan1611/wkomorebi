import win32pipe
import logging
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

if __name__ == "__main__":
    tko = KomorebiListener()
    tko.create_named_pipe()
    tko.connect_komorebi()