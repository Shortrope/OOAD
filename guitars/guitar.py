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
        builder: GBuilder,
        model: str,
        type: GType,
        top_wood: GWood,
        back_wood: GWood,
    ) -> None:
        self._sn = sn
        self._price = price
        self._spec = GuitarSpec(builder, model, type, top_wood, back_wood)

    def __str__(self):
        spec = self.spec
        return f"{self.sn}, {self.price}, {spec.builder.value}, {spec.model}, {spec.type.value}, {spec.back_wood.value}, {spec.top_wood.value}"

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
