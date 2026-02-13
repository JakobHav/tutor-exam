from typing import Callable


def block(f: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        print("Diese Funktion wurde blockiert!")
    return wrapper


# Alternativ:
block2 = lambda f: lambda: print("Diese Funktion wurde blockiert!")


def filter_dict[K, V](f: Callable[[K, V], bool], dic: dict[K, V]) -> dict[K, V]:
    return {k: v for k, v in dic.items() if f(k, v)}


def transpose[T](matrix: list[list[T]]) -> list[list[T]]:
    return [[x[i] for x in matrix] for i in range(len(matrix[0]))]


if __name__ == "__main__":
    d = {"a": 1, "b": 2, "c": 3, "d": 4}
    assert filter_dict(lambda x, y: y % 2 == 0, d) == {"b": 2, "d": 4}

    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]
