import time


class BarkSensor:
    def __init__(self, dogdoor) -> None:
        self.door = dogdoor

    def recognizer(self, sound):
        print(f"    BarkSensor: Heard a {sound}")
        if sound == "bark":
            print(f"    BarkSensor: Opening the door")
            self.door.open_with_auto_close()
