# Ex6: Bäume und Rekursion (25P)

from dataclasses import dataclass
from typing import Optional, Callable


@dataclass
class Node[T]:
    mark: T
    left: "Tree[T]" = None
    right: "Tree[T]" = None


type Tree[T] = Optional[Node[T]]


def count_leaves(tree):
    ...


def tree_map(f, tree):
    ...


def tree_to_list(tree):
    ...


def test_ordered(lst):
    ...


if __name__ == "__main__":
    assert count_leaves(None) == 0
    assert count_leaves(Node(1)) == 1
    assert count_leaves(Node("zero", Node("one"), Node("two"))) == 2

    t = Node(1, Node(2), Node(3))
    t2 = tree_map(lambda x: x * 2, t)
    assert t2 == Node(2, Node(4), Node(6))

    assert test_ordered(tree_to_list(Node(5, Node(4), Node(6))))
    assert not test_ordered(tree_to_list(Node(2, Node(4), Node(6))))
    assert not test_ordered(tree_to_list(Node(5, Node(6), Node(4))))

    assert test_ordered([0, 1, 2])
    assert not test_ordered([0, 3, 2])
