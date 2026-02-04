# Ex1: Warm-Up (20P)

from typing import Optional, Callable
from dataclasses import dataclass


def my_all(xs):
    ...


def einkaufsliste():
    ...


def mult_rec(a, b):
    ...


def mult_it(a, b):
    ...


@dataclass
class Node[T]:
    mark: T
    left: "Tree[T]"
    right: "Tree[T]"


type Tree[T] = Optional[Node[T]]


def apply_n_times(f, arg, n):
    ...


if __name__ == "__main__":
    assert all([True, False]) is False
    assert all([]) is True

    print(einkaufsliste())

    assert mult_rec(5, 4) == 20
    assert mult_it(5, 4) == 20
    assert mult_it(5, 5) == mult_rec(5, 5) == 5 * 5

    apply_n_times(print, "Hallo Welt!", 4)
