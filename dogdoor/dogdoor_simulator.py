from barksensor import BarkSensor
from dogdoor import DogDoor
from remote import Remote

door = DogDoor()
remote = Remote(door)
bark_sensor = BarkSensor(door)


def main() -> None:
    print("DogDoor/Remote Simulator")
    print(f"Is the Dog Door open? {door.is_open()}")
    print()

    print("Fido barks to go outside...")
    print("Pressing Button...")
    remote.press_button()
    print(f"Is the Dog Door open? {door.is_open()}")

    print("\nFido has gone outside...")
    print(f"Is the Dog Door open? {door.is_open()}")

    print("\nFido is all done...")
    remote.press_button()
    print("Button pressed...")
    print(f"Is the Dog Door open? {door.is_open()}")

    print("\nFido is back inside...")
    print(f"Is the Dog Door open? {door.is_open()}")
    print()
    print()

    print("DogDoor/Bark Sensor Simulator")
    print(f"Is the Dog Door open? {door.is_open()}")
    print()

    print("Fido barks to go outside...")
    print("Sensor Hears a bark...")
    bark_sensor.recognizer("bark")
    print(f"Is the Dog Door open? {door.is_open()}")

    print("\nFido has gone outside...")
    print(f"Is the Dog Door open? {door.is_open()}")

    print("\nFido is all done...")
    print("Fido barks to get back inside...")
    bark_sensor.recognizer("bark")
    print(f"Is the Dog Door open? {door.is_open()}")

    print("\nFido is back inside...")
    print(f"Is the Dog Door open? {door.is_open()}")
    print()


if __name__ == "__main__":
    main()
