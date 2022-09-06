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
        builder: GBuilder,
        model: str,
        type: GType,
        back_wood: GWood,
        top_wood: GWood,
    ) -> None:
        guitar = Guitar(sn, price, builder, model, type, back_wood, top_wood)
        self._guitars.append(guitar)

    def get_guitar(self, sn: str) -> Optional[Guitar]:
        for guitar in self._guitars:
            if guitar.get_sn() == sn:
                return guitar
        return None

    def search(self, search_spec: GuitarSpec) -> list:
        matches = []
        for guitar in self._guitars:
            if search_spec.builder != guitar.spec.builder:
                continue

            if search_spec.model != guitar.spec.model:
                continue

            if search_spec.type != guitar.spec.type:
                continue

            if search_spec.back_wood != guitar.spec.back_wood:
                continue

            if search_spec.top_wood != guitar.spec.top_wood:
                continue

            matches.append(guitar)

        return matches

    def get_inventory(self) -> list:
        return self._guitars
