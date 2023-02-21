import time


# class ProgramConsole():

async def run_console() -> None:
    is_execute: bool = True
    print("press control + C for end application")
    while (is_execute):
        time.sleep(0.05)
