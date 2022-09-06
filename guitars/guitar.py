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
        return f"{self.sn}, {self.price}, {self._spec.builder.value}, {self._spec.model}, {self._spec.type.value}, {self._spec.back_wood.value}, {self._spec.top_wood.value}"

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
        
    # @property 
    # def builder(self) -> GBuilder:
    #     return self._spec.builder

    # @property 
    # def model(self) -> str:
    #     return self._spec.model

    # @property 
    # def type(self) -> GType:
    #     return self._spec.type

    # @property 
    # def top_wood(self) -> GWood:
    #     return self._spec.top_wood

    # @property 
    # def back_wood(self) -> GWood:
    #     return self._spec.back_wood
