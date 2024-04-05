def _recursion_highest_num(_lst: list):
    if _lst[0] <= _lst[1]:
        _lst = _lst[1:]
    elif _lst[0] > _lst[1]:
        _lst = _lst[0:1] + _lst[2:]

    if len(_lst) == 1:
        return _lst
    else:
        return _recursion_highest_num(_lst)

_list = input("Write down an array(e.g. [1,6,8,2]): ")
print(int(_recursion_highest_num(list(_list))))