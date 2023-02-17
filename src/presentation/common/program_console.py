import time


class ProgramConsole():

    async def run(self):
        is_execute: bool = True

        print("press ctr + C for stop application")
        while (is_execute):
            time.sleep(0.05)
