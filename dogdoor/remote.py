class Remote:
    def __init__(self, door) -> None:
        self._door = door

    def press_button(self) -> None:
        if self._door.is_open():
            self._door.close()
        else:
            self._door.open()
