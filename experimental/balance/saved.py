import numpy
from numpy.random import Generator
from simple import SimpleBalance
from typing import List, Tuple, Dict


class SavedBalance(SimpleBalance):
    prev: List[Tuple[str, str, str, float]]
    shuffler: Generator

    def __init__(self, shuffler: Generator = numpy.random.default_rng()) -> None:
        super().__init__()
        self.prev = []
        self.shuffler = shuffler

    def update(self, elem0: str, elem1: str, elem2: str, value: float):
        self.prev.append((elem0, elem1, elem2, value))
        super().update(elem0, elem1, elem2, value)

    @property
    def result(self) -> Dict[str, float]:
        size = len(self.prev)
        for i in range(size - 1):
            j = self.shuffler.integers(i, size)
            self.prev[i], self.prev[j] = self.prev[j], self.prev[i]
        for e0, e1, e2, v in self.prev:
            super().update(e0, e1, e2, v)
        return self._elems
