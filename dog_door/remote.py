import threading
import time


class Remote:
    def __init__(self, door) -> None:
        self._door = door

    def press_button(self) -> None:
        print("Remote: Button Pressed...")
        if self._door.is_open():
            print("Remote: Closing door...")
            self._door.close()
        else:
            print("Remote: Opening door...")
            self._door.open_with_auto_close()
