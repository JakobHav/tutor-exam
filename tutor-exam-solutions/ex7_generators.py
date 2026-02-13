from typing import Iterable, Iterator


def take[T](xs: Iterable[T], n: int) -> Iterator[T]:
    count = 0
    for element in xs:
        if count == n:
            break
        yield element
        count += 1


def interleave[T](xs: Iterable[T], ys: Iterable[T]) -> Iterator[T]:
    xi = iter(xs)
    yi = iter(ys)
    try:
        while True:
            yield next(xi)
            yield next(yi)
    except StopIteration:
        pass

    yield from xi
    yield from yi


def is_prime(x: int) -> bool:
    for y in range(2, x // 2 + 1):
        if x % y == 0:
            return False
    return True


def primes() -> Iterator[int]:
    x = 1
    while True:
        if is_prime(x):
            yield x
        x += 1


if __name__ == "__main__":
    assert list(take(range(10), 3)) == [0, 1, 2]
    assert list(take("Hello World", 5)) == ['H', 'e', 'l', 'l', 'o']
    assert list(take([1, 2], 5)) == [1, 2]

    assert list(interleave([1, 2, 3], ['a', 'b', 'c'])) == [
        1, 'a', 2, 'b', 3, 'c']
    assert list(interleave([1, 2], ['a', 'b', 'c', 'd'])) == [
        1, 'a', 2, 'b', 'c', 'd']
    assert list(interleave([1, 2, 3], [])) == [1, 2, 3]

    prim_gen = primes()
    assert [next(prim_gen) for _ in range(7)] == [1, 2, 3, 5, 7, 11, 13]
