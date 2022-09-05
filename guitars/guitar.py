from gbuilder import GBuilder
from gtype import GType
from gwood import GWood


class Guitar:
    def __init__(
        self,
        sn: str,
        price: float,
        builder: GBuilder,
        model: str,
        type: GType,
        back_wood: GWood,
        top_wood: GWood,
    ) -> None:
        self._sn = sn
        self._price = price
        self._builder = builder
        self._model = model
        self._type = type
        self._back_wood = back_wood
        self._top_wood = top_wood

    def __str__(self):
        return f"{self.sn}, {self.price}, {self.builder.value}, {self.model}, {self.type.value}, {self.back_wood.value}, {self.top_wood.value}"

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
    def builder(self) -> GBuilder:
        return self._builder

    @property
    def model(self) -> str:
        return self._model

    @property
    def type(self) -> GType:
        return self._type

    @property
    def back_wood(self) -> GWood:
        return self._back_wood

    @property
    def top_wood(self) -> GWood:
        return self._top_wood
