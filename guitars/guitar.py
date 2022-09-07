from distutils.command.build import build

from gbuilder import GBuilder
from gtype import GType
from guitarspec import GuitarSpec
from gwood import GWood


class Guitar:
    def __init__(
        self,
        sn: str,
        price: float,
        spec: GuitarSpec
    ) -> None:
        self._sn = sn
        self._price = price
        self._spec = spec

    def __str__(self):
        spec = self.spec
        return f"{self.sn}, {self.price}, {spec.builder.value}, {spec.model}, {spec.type.value}, {spec.num_strings}, {spec.back_wood.value}, {spec.top_wood.value}"

    @property
    def sn(self) -> str:
        return self._sn

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price) -> None:
        self._price = price

    @property
    def spec(self) -> GuitarSpec:
        return self._spec
