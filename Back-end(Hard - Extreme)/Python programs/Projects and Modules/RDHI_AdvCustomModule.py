######################################################################
def list_maker(numbers):  #fully finished.
    numbers += ","
    num_container = []
    temp_ = ""
    for x in numbers:

        if x in ",":
            num_container.append(int(temp_))    #the "int" here is changeable.
            temp_ = ""

        elif x == " ":
            pass

        else:
            temp_ += x
    return num_container
def highest(_list):
    if _list[0] >= _list[1]:
        return _list[0]
    elif _list[1] > _list[0]:
        return _list[1]
def elementary_numbers(limit):  # fully finished. No modifications are needed.
        _divider = [2, 3]
        limit -= 4
        limit_perm = limit
        fu_number = 4
        recorder = []
        while limit > 0:
            recorder = []
            for _x in _divider:
                if fu_number / _x in range(limit_perm):
                    recorder += "0"  # non-fundamental or installed.
                elif fu_number / _x not in range(limit_perm):
                    recorder += "1"  # fundamental.
            if "0" in recorder:
                limit -= 1
            elif "1" in recorder:
                _divider.append(fu_number)
                limit -= 1
            fu_number += 1
            recorder = []
            if _x == _divider[-2]:
                _divider = _divider
        return _divider
#######################################################################

def gcf_value_int(*_list):  # finished
    _list, iterate = list(_list), len(_list) - 1
    while iterate > 0:
        gcf, container,iterate = 1, [_list[0], _list[1]], (iterate - 1)
        divider = elementary_numbers(highest(container))
        #gcf
        for x in divider:
            while type(container[0] / x) == "int" and type(container[1] / x) == "int" :
                container[0], container[1], gcf= container[0] / x, container[1] / x, gcf * x
        #gcf
        _list = _list[2:]
        _list.insert(0, gcf)
    gcf = _list[0]
    return gcf

#########################################################################

def lcm_value_int(*_list):  #finished
    _list = list(_list)
    _list.sort()
    container = [_list[0], _list[1]]
    lcm = gcf_value_int(_list)
    lcm_perm = lcm
    record = ["0"]
    if lcm == 1:
        for x in _list:
            lcm = lcm * x
    else:
        pass
    while "0" in record:
        record =[]
        for x in _list:
            if int(lcm) / x not in range(1, 100000):
                record += "0"
            elif lcm / x in range(1, 100000):
                record += "1"
            else:
                pass
        lcm += lcm_perm
    lcm -= lcm_perm
    return lcm
###########################################################################

def num_filter(number):
    number = str(number)
    _num = ["0","1","2","3","4","5","6","7","8","9", "."]
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
        number= len_inverter(number)
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
                "0":"",
                "1":"one ",
                "2":"two ",
                "3":"three ",
                "4":"four ",
                "5":"five ",
                "6":"six ",
                "7":"seven ",
                "8":"eight ",
                "9":"nine "
            }
            second_num = {
                "0":"",
                "1":"ten ",
                "2":"twenty ",
                "3":"thirty ",
                "4":"forty ",
                "5":"fifty ",
                "6":"sixty ",
                "7":"seventy ",
                "8":"eighty ",
                "9":"ninety "
            }
            third_num = {
                "0":"",
                "1":"one hundred ",
                "2":"two hundred ",
                "3":"three hundred ",
                "4":"four hundred ",
                "5":"five hundred ",
                "6":"six hundred ",
                "7":"seven hundred ",
                "8":"eight hundred ",
                "9":"nine hundred "
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
        spell_num = spell_num.replace("ten two","twelve")
        spell_num = spell_num.replace("ten three","thirteen")
        spell_num = spell_num.replace("ten four","fourteen")
        spell_num = spell_num.replace("ten five","fifteen")
        spell_num = spell_num.replace("ten six","sixteen")
        spell_num = spell_num.replace("ten seven","seventeen")
        spell_num = spell_num.replace("ten eight","eighteen")
        spell_num = spell_num.replace("ten nine","nineteen")
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

def bracket_ranging_A(_str):  #'(1+300%)/2*5'
    start_bracket = _str.find("(")  #0
    end_bracket = _str.find(")")  #7
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

def _sum(_list):  #[first number, second number, processor symbol]expected, [#'2', '300%', '+']

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
        _list[1] = _list[1][0:-1]  #['2', '300']
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



#################################################################################