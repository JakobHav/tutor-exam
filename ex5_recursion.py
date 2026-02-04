# Ex5: Endrekursion (15P)

def sum_list_rec(lst):
    ...


def sum_list_tail(lst, acc):
    ...


def sum_list_iter(lst):
    ...


if __name__ == "__main__":
    lst = [1, 5, 3, 4]
    assert sum_list_rec(lst) == 13
    assert sum_list_rec(lst) == sum_list_tail(lst) == sum_list_iter(lst)
