class DogDoor:
    def __init__(self, open: bool = False) -> None:
        self._open = open

    def open(self) -> None:
        self._open = True

    def close(self) -> None:
        self._open = False

    def is_open(self) -> bool:
        return self._open
