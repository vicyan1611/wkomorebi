import subprocess
class WKomorebic:
    def __init__(self) -> None:
        self.path = 'komorebic.exe'
        pass

    def subscribe_pipe(self, pipedname: str) -> None:
        subprocess.run(args=[self.path, 'subscribe-pipe', pipedname], shell=True)
    
    def flip_layout(self) -> None:
        subprocess.run(args=[self.path, 'flip-layout', 'horizontal'], shell=True)

    def start_komorebi(self) -> None:
        subprocess.run(args=[self.path, 'start'], shell=True)

    def stop_komorebi(self) -> None:
        subprocess.run(args=[self.path, 'stop'], shell=True)

    def pause_komorebi(self) -> None:
        subprocess.run(args=[self.path, 'toggle-pause'], shell=True)

if __name__ == "__main__":
    tkomo = WKomorebic()
    tkomo.flip_layout()