from typing import Dict


class Balance:
    _elems: Dict[str, float]

    def __init__(self) -> None:
        self._elems = dict()

    def update(self, elem0: str, elem1: str, elem2: str, value: float):
        raise NotImplementedError()

    @property
    def result(self) -> Dict[str, float]:
        return self._elems
