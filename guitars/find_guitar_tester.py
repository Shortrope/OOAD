from guitar import Guitar
from gbuilder import GBuilder
from gtype import GType
from gwood import GWood
from inventory import Inventory
from guitarspec import GuitarSpec


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
    inventory.add_guitar(
        "0004", 444.00, GBuilder.FENDER, "stratocaster", GType.ELECTRIC, GWood.ALDER, GWood.ALDER
    )


def main():
    inventory = Inventory()
    initialize_inventory(inventory)
    
    spec = GuitarSpec(GBuilder.FENDER, "stratocaster", GType.ELECTRIC, GWood.ALDER, GWood.ALDER)
    matches = inventory.search(spec)

    if matches:
        print("You may like these guitars:")
        for guitar in matches:
            print(f'{guitar.spec.builder.value.title()} {guitar.spec.model.title()}, sn#: {guitar.sn}')
            print(f'    {guitar.spec.back_wood.value} back and sides')
            print(f'    {guitar.spec.top_wood.value} top')
            print(f'Price: ${guitar.price}')
            print()
    else:
        print("Sorry, we have no guitars for you.")


if __name__ == "__main__":
    main()
