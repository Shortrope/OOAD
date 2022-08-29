class Guitar:
    def __init__(
        self,
        sn: str,
        price: float,
        builder: str,
        model: str,
        type: str,
        back_wood: str,
        top_wood: str,
    ) -> None:
        self._sn = sn
        self._price = price
        self._builder = builder
        self._model = model
        self._type = type
        self._back_wood = back_wood
        self._top_wood = top_wood

    def __str__(self):
        return f"{self.sn}, {self.price}, {self.builder}, {self.model}, {self.type}, {self.back_wood}, {self.top_wood}"

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
    def builder(self) -> str:
        return self._builder

    @property
    def model(self) -> str:
        return self._model

    @property
    def type(self) -> str:
        return self._type

    @property
    def back_wood(self) -> str:
        return self._back_wood

    @property
    def top_wood(self) -> str:
        return self._top_wood
