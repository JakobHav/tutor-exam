def sum_list_rec(lst: list[int]) -> int:
    return (lst[0] + sum_list_rec(lst[1:])) if lst else 0


def sum_list_tail(lst: list[int], acc: int = 0) -> int:
    return sum_list_tail(lst[1:], acc + lst[0]) if lst else acc


def sum_list_iter(lst: list[int], acc: int = 0) -> int:
    while lst:
        lst, acc = (lst[1:], acc + lst[0])
    return acc


if __name__ == "__main__":
    lst = [1, 5, 3, 4]
    assert sum_list_rec(lst) == 13
    assert sum_list_rec(lst) == sum_list_tail(lst) == sum_list_iter(lst)
