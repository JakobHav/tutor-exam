# Ex8: Funktionale Programmierung (20P)

from typing import Callable


def block(f):
    ...


def filter_dict(f, dic):
    ...


def transpose(matrix):
    ...


if __name__ == "__main__":
    d = {"a": 1, "b": 2, "c": 3, "d": 4}
    assert filter_dict(lambda x, y: y % 2 == 0, d) == {"b": 2, "d": 4}

    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]
