from balance import Balance


class SimpleBalance(Balance):
    def __init__(self) -> None:
        super().__init__()
        self._elems = dict()

    def update(self, elem0: str, elem1: str, elem2: str, value: float):
        v0 = self._elems.get(elem0, 0.0)
        v1 = self._elems.get(elem1, 0.0)
        v2 = self._elems.get(elem2, 0.0)
        diff = (value - (v0 + v1 + v2)) / 3
        self._elems[elem0] = v0 + diff
        self._elems[elem1] = v1 + diff
        self._elems[elem2] = v2 + diff
