from balance import Balance
from simple import SimpleBalance
import sys
from typing import List, Tuple
import random


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


def main(argv: List[str]):
    size = int(argv[1]) if len(argv) >= 2 else 10
    answer: List[float] = list()
    for _ in range(size):
        answer.append(float(random.randint(1, 20)) / 2)
    comb0: List[Tuple[int, int, int]] = list()
    for x in range(size - 2):
        for y in range(x + 1, size - 1):
            for z in range(y + 1, size):
                comb0.append((x, y, z))
    comb1 = comb0.copy()
    random.shuffle(comb0)
    random.shuffle(comb1)
    result0 = test(answer, comb0, SimpleBalance())
    result1 = test(answer, comb0 + comb1, SimpleBalance())
    for i in range(size):
        a, r0, r1 = answer[i], result0[i], result1[i]
        e0 = abs(a - r0) / a * 100
        e1 = abs(a - r1) / a * 100
        print(f"{i}: {a:.1f}, ({r0:.3f}, {e0:.3f}%), ({r1:.3f}, {e1:.3f})")


if __name__ == "__main__":
    main(sys.argv)
