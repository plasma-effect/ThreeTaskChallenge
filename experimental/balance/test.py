from balance import Balance
from simple import SimpleBalance
from loop import LoopBalance
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
        for i in range(len(self.answer)):
            ret = max(
                ret, abs(self.answer[i] - balance.result[str(i)]) * self.answer[i]
            )
        return ret


def test(
    answer: List[float], comb: List[Tuple[int, int, int]], balance: Balance
) -> List[float]:
    for x, y, z in comb:
        s = answer[x] + answer[y] + answer[z]
        balance.update(str(x), str(y), str(z), s)
    result: List[float] = [0.0 for _ in range(len(answer))]
    for name, value in balance.result.items():
        result[int(name)] = value
    return result


def maxdiff(answer: List[float], result: List[float]) -> float:
    ret = 0.0
    for i in range(min(len(answer), len(result))):
        ret = max(ret, abs(answer[i] - result[i]) * answer[i])
    return ret


def main(argv: List[str]):
    size = int(argv[1]) if len(argv) >= 2 else 10
    tester = Tester(size)
    simple_result = tester.test(SimpleBalance())
    loop_result = tester.test(LoopBalance())
    print(f"simple: {simple_result * 100:.3f}%")
    print(f"  loop: {loop_result * 100:.3f}%")


if __name__ == "__main__":
    main(sys.argv)
