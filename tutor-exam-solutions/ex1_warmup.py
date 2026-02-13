from typing import Optional, Callable
from dataclasses import dataclass


def my_all(xs: list[bool]) -> bool:
    for x in xs:
        if not x:
            return False
    return True


def einkaufsliste() -> set[str]:
    ret = set()
    while True:
        i = input("Einkauf: ")
        if i == "Fertig":
            return ret
        ret.add(i)


def mult_rec(a: int, b: int) -> int:
    return a + mult_rec(a, b - 1) if b > 0 else 0


def mult_it(a: int, b: int) -> int:
    ret = 0
    for i in range(b):
        ret += a
    return ret


@dataclass
class Node[T]:
    number: int
    mark: T
    left: "Tree[T]"
    middle: "Tree[T]"
    right: "Tree[T]"


type Tree[T] = Optional[Node[T]]


def apply_n_times[T](f: Callable[[T], None], arg: T, n: int) -> None:
    for _ in range(n):
        f(arg)


if __name__ == "__main__":
    assert all([True, False]) is False
    assert all([]) is True

    print(einkaufsliste())

    assert mult_rec(5, 4) == 20
    assert mult_it(5, 4) == 20
    assert mult_it(5, 5) == mult_rec(5, 5) == 5 * 5

    apply_n_times(print, "Hallo Welt!", 4)
