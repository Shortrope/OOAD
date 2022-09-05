from typing import Optional
from gbuilder import GBuilder
from gtype import GType
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

    def search(self, spec_guitar: Guitar) -> list:
        matches = []
        for guitar in self._guitars:
            spec_builder = spec_guitar.builder
            if (
                spec_builder is not None
                and spec_builder != ""
                and spec_builder != guitar.builder
            ):
                continue
            # else:
            #     print(f'Match "builder": {spec_builder}')

            spec_model = spec_guitar.model
            guitar_model = guitar.model
            if (
                spec_model is not None
                and spec_model != ""
                and spec_model != guitar.model
            ):
                continue
            # else:
            #     print(f'Match "model": {spec_model}')

            spec_type = spec_guitar.type
            if spec_type is not None and spec_type != "" and spec_type != guitar.type:
                continue
            # else:
            #     print(f'Match "type": {spec_type}')

            spec_back_wood = spec_guitar.back_wood
            if (
                spec_back_wood is not None
                and spec_back_wood != ""
                and spec_back_wood != guitar.back_wood
            ):
                continue
            # else:
            #     print(f'Match "back_wood": {spec_back_wood}')

            spec_top_wood = spec_guitar.top_wood
            if (
                spec_top_wood is not None
                and spec_top_wood != ""
                and spec_top_wood != guitar.top_wood
            ):
                continue
            # else:
            #     print(f'Match "top_wood": {spec_top_wood}')

            matches.append(guitar)

        # print()
        return matches

    def get_inventory(self) -> list:
        return self._guitars