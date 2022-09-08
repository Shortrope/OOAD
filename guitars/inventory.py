from typing import Optional

from gbuilder import GBuilder
from gtype import GType
from guitar import Guitar
from guitarspec import GuitarSpec
from gwood import GWood


class Inventory:
    def __init__(self) -> None:
        self._guitars: list = []

    def add_guitar(
        self,
        sn: str,
        price: float,
        spec: GuitarSpec
    ) -> None:
        guitar = Guitar(sn, price, spec)
        self._guitars.append(guitar)

    def get_guitar(self, sn: str) -> Optional[Guitar]:
        for guitar in self._guitars:
            if guitar.get_sn() == sn:
                return guitar
        return None

    def search(self, search_spec: GuitarSpec) -> list:
        matches = []
        for guitar in self._guitars:
            if guitar.spec.equals(search_spec):
                matches.append(guitar)

        return matches

    def get_inventory(self) -> list:
        return self._guitars
