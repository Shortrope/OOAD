import time


class DogDoor:
    def __init__(self, open: bool = False) -> None:
        self._open = open

    def open(self) -> None:
        print("DogDoor: Opening door...")
        self._open = True

    def open_with_auto_close(self, delay: int = 2) -> None:
        print(f"DogDoor: Opening door with delay ({delay}s)...")
        self._open = True
        time.sleep(delay)
        self.close()

    def close(self) -> None:
        print("DogDoor: Closing door...")
        self._open = False

    def is_open(self) -> bool:
        return self._open
