import math
import numpy as np






def _lcm(a):
    pass


def _unique(_list):
    _list = np.array(_list)
    _list = np.unique(_list)
    return list(_list)



def _werid_factor(_divider:list, _divided:list) -> int:
    _lst_divi = _divider
    _divider = lcm(_divider)
    _perm_divider = _divider
    _count = 0

    _not_divid = 0
    while _not_divid == 0:
        for x in _divided:
            if x % _divider == 0:
                pass
            else:
                _not_divid = 1
        _count += 1
        _divider += _perm_divider
    print(_lst_divi)
    print(_divider)
    if _divider == _lst_divi[-1]:
        _count += 1



    return _count








_temp_ = []
_input_divider = input("Input divider list: ").strip().split(",")
for x in _input_divider:
    _temp_.append(int(x))
_input_divider = _temp_

_temp_ = []
_input_divided = input("Input divided list: ").split(",")
for x in _input_divided:
    _temp_.append(int(x))
_input_divided = _temp_

_input_divider = _unique(_input_divider)
_input_divided = _unique(_input_divided)

print(_werid_factor(_input_divider, _input_divided))
