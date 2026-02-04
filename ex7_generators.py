# Ex7: Generatoren (20P)

from typing import Iterable, Iterator


def take(xs, n):
    ...


def interleave(xs, ys):
    ...


def primes():
    ...


if __name__ == "__main__":
    assert list(take(range(10), 3)) == [0, 1, 2]
    assert list(take("Hello World", 5)) == ['H', 'e', 'l', 'l', 'o']
    assert list(take([1, 2], 5)) == [1, 2]

    assert list(interleave([1, 2, 3], ['a', 'b', 'c'])) == [1, 'a', 2, 'b', 3, 'c']
    assert list(interleave([1, 2], ['a', 'b', 'c', 'd'])) == [1, 'a', 2, 'b', 'c', 'd']
    assert list(interleave([1, 2, 3], [])) == [1, 2, 3]

    prim_gen = primes()
    assert [next(prim_gen) for _ in range(7)] == [1, 2, 3, 5, 7, 11, 13]
