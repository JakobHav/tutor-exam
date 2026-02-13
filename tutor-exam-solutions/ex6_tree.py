from dataclasses import dataclass
from typing import Optional, Callable


@dataclass
class Node[T]:
    mark: T
    left: "Tree[T]" = None
    right: "Tree[T]" = None


type Tree[T] = Optional[Node[T]]


def count_leaves[T](tree: Tree[T]) -> int:
    match tree:
        case None:
            return 0
        case Node(_, None, None):
            return 1
        case Node(_, l, r):
            return count_leaves(l) + count_leaves(r)


def tree_map[T](f: Callable[[T], T], tree: Tree[T]) -> Tree[T]:
    match tree:
        case None:
            return None
        case Node(m, l, r):
            return Node(f(m), tree_map(f, l), tree_map(f, r))


def tree_to_list(tree: Tree[int]) -> list[int]:
    match tree:
        case None:
            return []
        case Node(m, l, r):
            return tree_to_list(l) + [m] + tree_to_list(r)


def test_ordered(lst: list[int]) -> bool:
    return lst == list(sorted(lst))


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
