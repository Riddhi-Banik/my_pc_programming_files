

def elementary_numbers(_limit):
    _divider = [2, 3]
    for x in range(4, int(_limit) + 5):
        _will_add = True
        for y in _divider:
            if x % y == 0:
                _will_add = False
        if _will_add:
            _divider.append(x)
    return _divider


def _elements(_num:int):
    _divider = elementary_numbers(_num)
    _elements = []
    for x in _divider:
        _will_next = False
        while not _will_next:
            if _num % x == 0:
                _num = int(_num /  x)
                _elements.append(x)
            else:
                _will_next = True
    return _elements
def gcf_value_int(_array:list):
    _array = list(set(_array))
    _array.sort()
    _gcf = 0
    while len(_array) > 1:
        container = [list(_elements(_array[0])), list(_elements(_array[-1]))]
        _array.pop(0)
        _array.pop(-1)
        _gcf = 1
        for x, y in zip(container[0], container[1]):
            if x in container[1]:
                _gcf *= x
        _array.append(_gcf)
    return _gcf

def lcm_value_int(_array):
    _array = list(set(_array))
    while len(_array) > 1:
        container = [_array[0], _array[-1]]
        _con_gcf = gcf_value_int(container)
        _lcm = ((container[0] / _con_gcf) * (container[1] / _con_gcf)) * _con_gcf
        _array.pop(0)
        _array.pop(-1)
        _array.append(_lcm)
    return _lcm







#print(elementary_numbers(20))
print(_elements(7000))
print(gcf_value_int([20,5]))
print(lcm_value_int([20, 4, 2, 20,5]))

