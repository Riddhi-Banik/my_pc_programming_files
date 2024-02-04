def list_creator(list_of_number):
    list_of_number.strip()
    list_of_number, y = list_of_number.split(","), -1
    for x in list_of_number:
        y += 1
        list_of_number.insert(y, int(x))
        list_of_number.pop(y + 1)
    return list_of_number
def elementary_number_creator(max_):
    divider, _const, limit = [2, 3], 2, max_
    while 0 < limit:
        will_add, _const = True, _const + 1
        for x in divider:
            if _const % x == 0:
                will_add = False
        limit -= 1
        if will_add:
            divider.append(_const)
    return divider
def highest(list):
    if list[0] >= list[1]:
        return list[0]
    elif list[1] > list[0]:
        return list[1]
def hcf_value_int(list):
    _container = [list[0], list[-1]]
    while len(list) > 1:
        _divider, hcf, multiple_ = elementary_number_creator(highest(_container)), 1, "The multipliers are: [1"
        for x in _divider:
            while _container[0] % x == 0 and _container[-1] % x == 0:
                _container[0], _container[-1], hcf, multiple_ = _container[0] / x, _container[-1] / x, hcf * x, multiple_ + f" X {x}"
        list.pop(0)
        list.pop(-1)
        list.insert(0, hcf)
        _container = [list[0], list[-1]]
    res_ = [hcf, (multiple_ + "]")]
    return res_
def lcm_value_int(list):
    while len(list) > 1:
        _container = [list[0], list[-1]]
        _sash = hcf_value_int(_container)[0]
        _lcm = (list[0] * list[-1]) / _sash
        list.pop(0)
        list.pop(-1)
        list.insert(0, _lcm)
    return _lcm


ques = input("insert a list with comma separated: ")
print(hcf_value_int(list_creator(ques))[1] + f" = [{int(hcf_value_int(list_creator(ques))[0])}]")
print(f"The LCM is: [{int(lcm_value_int(list_creator(ques)))}]")