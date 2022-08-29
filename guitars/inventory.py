from typing import Optional

from guitar import Guitar


class Inventory:
    def __init__(self) -> None:
        self._guitars: list = []

    def add_guitar(
        self,
        sn: str,
        price: float,
        builder: str,
        model: str,
        type: str,
        back_wood: str,
        top_wood: str,
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

            spec_model = spec_guitar.model
            if (
                spec_model is not None
                and spec_model != ""
                and spec_model != guitar.model
            ):
                continue

            spec_type = spec_guitar.type
            if spec_type is not None and spec_type != "" and spec_type != guitar.type:
                continue

            spec_back_wood = spec_guitar.back_wood
            if (
                spec_back_wood is not None
                and spec_back_wood != ""
                and spec_back_wood != guitar.back_wood
            ):
                continue

            spec_top_wood = spec_guitar.top_wood
            if (
                spec_top_wood is not None
                and spec_top_wood != ""
                and spec_top_wood != guitar.top_wood
            ):
                continue

            matches.append(guitar)

        return matches
