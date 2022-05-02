from balance import Balance
from simple import SimpleBalance
from loop import LoopBalance
from saved import SavedBalance
import sys
from typing import List, Tuple
import random


class Tester:
    answer: List[float]
    data: List[Tuple[int, int, int, float]]

    def __init__(self, size: int = 10) -> None:
        self.answer = [0.0 for _ in range(size)]
        self.data = []
        for i in range(size):
            self.answer[i] = random.randint(1, 20) / 2.0
        comb: List[Tuple[int, int, int]] = list()
        for x in range(size - 2):
            for y in range(x + 1, size - 1):
                for z in range(y + 1, size):
                    comb.append((x, y, z))
        random.shuffle(comb)
        count = [0 for _ in range(size)]
        for i, j, k in comb:
            count[i] += 1
            count[j] += 1
            count[k] += 1
            bias = random.random()
            self.data.append((i, j, k, bias))
            if min(count) == 3:
                break

    def test(self, balance: Balance) -> float:
        for i in range(len(self.data)):
            x, y, z, bias = self.data[i]
            balance.update(
                str(x),
                str(y),
                str(z),
                self.answer[x] + self.answer[y] + self.answer[z] + bias,
            )
        ret = 0.0
        result = balance.result
        for i in range(len(self.answer)):
            ret = max(ret, abs(self.answer[i] - result[str(i)]) * self.answer[i])
        return ret


def main(argv: List[str]):
    size = int(argv[1]) if len(argv) >= 2 else 10
    tester = Tester(size)
    print(f"simple: {tester.test(SimpleBalance()) * 100:.3f}%")
    print(f"  loop: {tester.test(LoopBalance()) * 100:.3f}%")
    print(f" saved: {tester.test(SavedBalance()) * 100:.3f}%")


if __name__ == "__main__":
    main(sys.argv)
