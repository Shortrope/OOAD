from gbuilder import GBuilder
from gtype import GType
from gwood import GWood

class GuitarSpec:
    def __init__(
        self,
        builder: GBuilder,
        model: str,
        type: GType,
        num_strings: int,
        back_wood: GWood,
        top_wood: GWood,
    ) -> None:
        self._builder = builder
        self._model = model
        self._type = type
        self._num_strings = num_strings
        self._back_wood = back_wood
        self._top_wood = top_wood

    def __str__(self):
        return f"{self.builder.value}, {self.model}, {self.type.value}, {self._num_strings} string, {self.back_wood.value}, {self.top_wood.value}"

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
    def num_strings(self) -> int:
        return self._num_strings

    @property
    def back_wood(self) -> GWood:
        return self._back_wood

    @property
    def top_wood(self) -> GWood:
        return self._top_wood

    def equals(self, other_spec) -> bool:
        if self.builder != other_spec.builder:
            return False
        
        if self.model != other_spec.model:
            return False
        
        if self.type != other_spec.type:
            return False
        
        if self.num_strings != other_spec.num_strings:
            return False

        if self.top_wood != other_spec.top_wood:
            return False

        if self.back_wood != other_spec.back_wood:
            return False
        
        return True