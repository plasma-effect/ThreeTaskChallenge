from typing import List, Tuple

from simple import SimpleBalance


class LoopBalance(SimpleBalance):
    prev: List[Tuple[str, str, str, float]]

    def __init__(self) -> None:
        super().__init__()
        self.prev = []

    def update(self, elem0: str, elem1: str, elem2: str, value: float):
        self.prev.append((elem0, elem1, elem2, value))
        for e0, e1, e2, v in self.prev:
            super().update(e0, e1, e2, v)
