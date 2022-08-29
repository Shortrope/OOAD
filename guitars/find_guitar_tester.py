from guitar import Guitar
from inventory import Inventory


def initialize_inventory(inventory: Inventory) -> None:
    inventory.add_guitar(
        "0001", 111.00, "fender", "stratocaster", "electric", "alder", "alder"
    )


def main():
    inventory = Inventory()
    initialize_inventory(inventory)

    spec = Guitar("", 0, "fender", "stratocastor", "electric", "alder", "alder")
    print(spec)
    matches = inventory.search(spec)
    print(matches)
    if matches:
        for guitar in matches:
            print(guitar)
    else:
        print("Sorry, we have no guitars for you.")


if __name__ == "__main__":
    main()
