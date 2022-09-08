from dogdoor import DogDoor
from remote import Remote

door = DogDoor()
remote = Remote(door)


def main() -> None:
    print("DogDoor/Remote Simulator")
    print(f"Is the Dog Door open? {door.is_open()}")
    print()

    print("Fido barks to go outside...")
    remote.press_button()
    print("Button pressed...")
    print(f"Is the Dog Door open? {door.is_open()}")

    print("\nFido has gone outside...")
    remote.press_button()
    print("Button pressed...")
    print(f"Is the Dog Door open? {door.is_open()}")

    print("\nFido is all done...")
    remote.press_button()
    print("Button pressed...")
    print(f"Is the Dog Door open? {door.is_open()}")

    print("\nFido is back inside...")
    remote.press_button()
    print("Button pressed...")
    print(f"Is the Dog Door open? {door.is_open()}")
    print()


if __name__ == "__main__":
    main()
