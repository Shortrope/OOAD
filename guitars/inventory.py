from typing import Optional
from gbuilder import GBuilder
from gtype import GType
from guitarspec import GuitarSpec
from gwood import GWood
from guitar import Guitar


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
            spec_builder = search_spec.builder
            if (
                spec_builder is not None
                and spec_builder != ""
                and spec_builder != guitar.spec.builder
            ):
                continue
            # else:
            #     print(f'Match "builder": {spec_builder}')

            spec_model = search_spec.model
            guitar_model = guitar.spec.model
            if (
                spec_model is not None
                and spec_model != ""
                and spec_model != guitar.spec.model
            ):
                continue
            # else:
            #     print(f'Match "model": {spec_model}')

            spec_type = search_spec.type
            if spec_type is not None and spec_type != "" and spec_type != guitar.spec.type:
                continue
            # else:
            #     print(f'Match "type": {spec_type}')

            spec_back_wood = search_spec.back_wood
            if (
                spec_back_wood is not None
                and spec_back_wood != ""
                and spec_back_wood != guitar.spec.back_wood
            ):
                continue
            # else:
            #     print(f'Match "back_wood": {spec_back_wood}')

            spec_top_wood = search_spec.top_wood
            if (
                spec_top_wood is not None
                and spec_top_wood != ""
                and spec_top_wood != guitar.spec.top_wood
            ):
                continue
            # else:
            #     print(f'Match "top_wood": {spec_top_wood}')

            matches.append(guitar)

        # print()
        return matches

    def get_inventory(self) -> list:
        return self._guitars