from nis import match
from guitar import Guitar
from gbuilder import GBuilder
from gtype import GType
from gwood import GWood
from inventory import Inventory


def initialize_inventory(inventory: Inventory) -> None:
    inventory.add_guitar(
        "0001", 111.00, GBuilder.FENDER, "stratocaster", GType.ELECTRIC, GWood.ALDER, GWood.ALDER
    )
    inventory.add_guitar(
        "0002", 222.00, GBuilder.GIBSON, "les paul", GType.ELECTRIC, GWood.MAHOGONEY, GWood.MAHOGONEY
    )
    inventory.add_guitar(
        "0003", 333.00, GBuilder.MARTIN, "doughnut", GType.ACOUSTIC, GWood.BRAZILIAN_ROSEWOOD, GWood.BRAZILIAN_ROSEWOOD
    )


def main():
    inventory = Inventory()
    initialize_inventory(inventory)
    
    print("Printing Inventory...")
    for guitar in inventory.get_inventory():
        print(guitar)
    print()

    spec = Guitar("", 0, GBuilder.FENDER, "stratocaster", GType.ELECTRIC, GWood.ALDER, GWood.ALDER)
    matches = inventory.search(spec)

    for guitar in matches:
        print(guitar)
    # if matches:
    #     for guitar in matches:
    #         print(guitar)
    # else:
    #     print("Sorry, we have no guitars for you.")


if __name__ == "__main__":
    main()
