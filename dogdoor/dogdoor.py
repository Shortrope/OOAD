class DogDoor:
    def __init__(self, open: bool = False) -> None:
        self._open = open

    def open(self) -> None:
        print("DogDoor: Opening door...")
        self._open = True

    def close(self) -> None:
        print("DogDoor: Closing door...")
        self._open = False

    def is_open(self) -> bool:
        return self._open
