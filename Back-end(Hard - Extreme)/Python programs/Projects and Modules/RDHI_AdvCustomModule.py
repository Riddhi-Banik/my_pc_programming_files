######################################################################
def _possible_elements(_num:int):
    _res = []
    for x in range(1, int(_num ** 0.5 + 1)):
        if _num % x == 0:
            _res.append(f"{x} x {int(_num / x)} = {_num}")
    return _res

def _elements(_num:int):
    if _num <= 0:
        return [0]
    _element = []
    for x in range(2, _num + 1):
        while True:
            if _num % x == 0:
                _element.append(x)
                _num /= x
            else:
                break
    return _element

def collapse_array(arr):  # copied from via chatgpt
    result = []
    for element in arr:
        if isinstance(element, list):
            result.extend(collapse_array(element))
        else:
            result.append(element)
    return result

def list_maker(numbers):  # fully finished. I DON'T CARE ABOUT THIS.
    numbers += ","
    num_container = []
    temp_ = ""
    for x in numbers:

        if x in ",":
            num_container.append(int(temp_))  # the "int" here is changeable.
            temp_ = ""

        elif x == " ":
            pass

        else:
            temp_ += x
    return num_container
def elementary_numbers(_limit:int):
    _divider = []
    for x in range(1, _limit + 1):
        _is_prime = True
        for y in _divider:
            if x % y == 0 and y != 1:
                _is_prime = False
        if _is_prime:
            _divider.append(x)
    return _divider.remove(1)

def gcf_value_int(_array:list) -> int: # required _elements() and flatter
    _array, gcf = [_elements(x) for x in _array], 1
    _used_elements = list(set(flatter(_array.copy())))
    for x in _used_elements:
        index, _count_used = 0, []
        for y in _array:
            _count_used.append(y.count(x))
        gcf *= x ** min(_count_used)
    return gcf


#########################################################################

def lcm_value_int(_array:list) -> int: # required _elements() and flatter
    _array, lcm = [_elements(x) for x in _array], 1
    _used_elements = list(set(flatter(_array.copy())))
    for x in _used_elements:
        index, _count_used = 0, []
        for y in _array:
            _count_used.append(y.count(x))
        lcm *= x ** max(_count_used)
    return lcm


###########################################################################

def num_filter(number):
    number = str(number)
    _num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    res = ""
    for x in number:
        if x in _num:
            res += x
    res = str(res)
    return res


######################################################

def len_inverter(string):
    y = ""
    for x in string:
        y = x + y
    return y


###########################################################
def num_speller(number):
    if ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] in number:
        number = len_inverter(number)
        number = num_filter(number)
        spell_num = ""
        lengh = 0
        temp_str = ""
        for x in number:
            first_list = [1, 4, 7, 10, 13]
            second_list = [2, 5, 8, 11, 14]
            third_list = [3, 6, 9, 12, 15]
            lengh += 1
            first_num = {
                "0": "",
                "1": "one ",
                "2": "two ",
                "3": "three ",
                "4": "four ",
                "5": "five ",
                "6": "six ",
                "7": "seven ",
                "8": "eight ",
                "9": "nine "
            }
            second_num = {
                "0": "",
                "1": "ten ",
                "2": "twenty ",
                "3": "thirty ",
                "4": "forty ",
                "5": "fifty ",
                "6": "sixty ",
                "7": "seventy ",
                "8": "eighty ",
                "9": "ninety "
            }
            third_num = {
                "0": "",
                "1": "one hundred ",
                "2": "two hundred ",
                "3": "three hundred ",
                "4": "four hundred ",
                "5": "five hundred ",
                "6": "six hundred ",
                "7": "seven hundred ",
                "8": "eight hundred ",
                "9": "nine hundred "
            }

            len_shift = ""
            if lengh == 4:
                len_shift = "thousand "
            elif lengh == 7:
                len_shift = "million "
            elif lengh == 10:
                len_shift = "billion "
            elif lengh == 13:
                len_shift = "trillion"

            if lengh in first_list:
                x = first_num[x] + len_shift
            elif lengh in second_list:
                x = second_num[x]
            elif lengh in third_list:
                x = third_num[x]
            else:
                pass
            spell_num = x + spell_num
        spell_num = spell_num.replace("ten one", "eleven")
        spell_num = spell_num.replace("ten two", "twelve")
        spell_num = spell_num.replace("ten three", "thirteen")
        spell_num = spell_num.replace("ten four", "fourteen")
        spell_num = spell_num.replace("ten five", "fifteen")
        spell_num = spell_num.replace("ten six", "sixteen")
        spell_num = spell_num.replace("ten seven", "seventeen")
        spell_num = spell_num.replace("ten eight", "eighteen")
        spell_num = spell_num.replace("ten nine", "nineteen")
        return spell_num
    else:
        return number


############################################################################

def _find(_list, _obj):
    _res = -1
    for x in _list:
        _res += 1
        if x == _obj:
            return _res
    if _res == -1:
        return _res


############################################################################

def bracket_ranging_A(_str):  # '(1+300%)/2*5'
    start_bracket = _str.find("(")  # 0
    end_bracket = _str.find(")")  # 7
    _res = [start_bracket, end_bracket]
    if start_bracket == -1 or end_bracket == -1:
        return -1
    else:
        return _res


############################################################################

def numbers_only(_ques):  # (1+300%)/2 *5 sample answer expected = ["1", "300%", "2", "5"]
    _ques += "+"
    _temp_cont = ""
    _list = []
    for x in _ques:
        if x in " ":
            pass
        elif x in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "%", "."]:
            _temp_cont += x
        elif x in ["(", ")", "/", "*", "+", "-"]:
            _list.append(_temp_cont)
            _temp_cont = ""
        if "" in _list:
            _list.remove("")
    return _list


#############################################################################

def symbol_only(_ques):
    _list = []
    for x in _ques:
        if x in ["/", "*", "+", "-"]:
            _list.append(x)
    return _list


#############################################################################

def _sum(_list):  # [first number, second number, processor symbol]expected, [#'2', '300%', '+']

    if "%" in _list[1] and "%" in _list[0]:
        _list[0] = _list[0][0:-1]
        _list[1] = _list[1][0:-1]
        if "/" in _list[2]:
            return str(float(_list[0]) / float(_list[1])) + "%"
        elif "*" in _list[2]:
            return str(float(_list[0]) * float(_list[1])) + "%"
        elif "+" in _list[2]:
            return str(float(_list[0]) + float(_list[1])) + "%"
        elif "-" in _list[2]:
            return str(float(_list[0]) - float(_list[1])) + "%"

    elif "%" in _list[0]:
        _list[0] = _list[0][0:-1]
        if "/" in _list[2]:
            return str(float(_list[0]) / float(_list[1])) + "%"
        elif "*" in _list[2]:
            return str(float(_list[0]) * float(_list[1])) + "%"
        elif "+" in _list[2]:
            return 0
        elif "-" in _list[2]:
            return 0

    elif "%" in _list[1]:
        _list[1] = _list[1][0:-1]  # ['2', '300']
        _list[1] = (float(_list[1]) / 100) * float(_list[0])
        if "/" in _list[2]:
            return str(float(_list[0]) / float(_list[1]))
        elif "*" in _list[2]:
            return str(float(_list[0]) * float(_list[1]))
        elif "+" in _list[2]:
            return str(float(_list[0]) + float(_list[1]))
        elif "-" in _list[2]:
            return str(float(_list[0]) - float(_list[1]))
    else:
        if "/" in _list[2]:
            return str(float(_list[0]) / float(_list[1]))
        elif "*" in _list[2]:
            return str(float(_list[0]) * float(_list[1]))
        elif "+" in _list[2]:
            return str(float(_list[0]) + float(_list[1]))
        elif "-" in _list[2]:
            return str(float(_list[0]) - float(_list[1]))


#################################################################################

def _repeat_code(code: str, parameters: list, target_change: str):
    """code: pass the actual code to mass execute
    parameters: pass a list of parameters to add parameters in the list everytime it gets executed
    target_change: pass a variable that will be located in the 'code's parameter area

    this function can significantly reduce repetition in a program"""

    _str = ""
    for x in parameters:
        _str += code.replace(target_change, str(x)) + "\n"
    return exec(_str)

#################################################################################

def flatter(_res:list):
    while True:
        _is_list_there = False
        for i in _res:
            if type(i) == type([1,]):
                _res.remove(i)
                _res.extend(i)
                _is_list_there = True
        if not _is_list_there:
            break
    return _res

#################################################################################


