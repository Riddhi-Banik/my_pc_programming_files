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
def symbol_only(_ques):
    _list = []
    for x in _ques:
        if x in ["/", "*", "+", "-"]:
            _list.append(x)
    return _list
def bracket_ranging(_str):  #'(1+300%)/2*5'
    start_bracket = _str.find("(")  #0
    end_bracket = _str.find(")")  #7
    _res = [start_bracket, end_bracket]
    if start_bracket == -1 or end_bracket == -1:
        return [0, len(_math_sentn)]
    else:
        return _res
def bracket_ranging_A(_str):  #'(1+300%)/2*5'
    start_bracket = _str.find("(")  #0
    end_bracket = _str.find(")")  #7
    _res = [start_bracket, end_bracket]
    if start_bracket == -1 or end_bracket == -1:
        return [0, len(_math_sentn)]
    else:
        return _res
def _find(_list, _obj):
    _res = -1
    for x in _list:
        _res += 1
        if x == _obj:
            return _res
    if _res == -1:
        return _res
def _sum(_list): #[first number, second number, processor symbol]expected, [#'2', '300%', '+']

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

_question = input("Insert a mathematical sentence: ")
#_question = '(12+3)+(4*6)'  #sample for debugging. Timeline expected:
_question = _question.replace(" ", "")
_math_sentn = _question  #'(1+300%)/2*5'
_num = numbers_only(_math_sentn)  #['1', '300%', '2', '5']
_sym = symbol_only(_math_sentn)  #['+', '/', '*']
_iterate = 0
_t_ques = bracket_ranging(_math_sentn)  #[0,7]
_t_ques = _math_sentn[_t_ques[0] -1:_t_ques[1] + 1]
while len(_num) > 1:
    if _iterate >= 1:
        a = 1
        a = a
        _math_sentn = (_math_sentn[0:(bracket_ranging(_math_sentn)[0]) + 0]) + str(ans) + (_math_sentn[(bracket_ranging(_math_sentn)[1]) + 1:len(_math_sentn)])  # currently string!  #!!!!
        #_math_sentn = str(ans) + _math_sentn # line is temperately paused.
    _iterate += 1
    ans = 0.0
    if "(" in _math_sentn:
        _addi_num = len(numbers_only(_math_sentn[:_find(_math_sentn, "(")]))
        _addi_sym = len(symbol_only(_math_sentn[:_find(_math_sentn, "(")]))
    else:
        _addi_num = 0
        _addi_sym = 0
    if "(" in _math_sentn:
        _t_ques = bracket_ranging(_math_sentn)  #[0,7]
        _t_ques = _math_sentn[_t_ques[0] + 1:_t_ques[1] + 0]  #'1+300%'
    else:
        _t_ques = _math_sentn
    _t_ques_num = numbers_only(_t_ques)  # [1, 300%]
    _t_ques_sym = symbol_only(_t_ques)  # [+]
    while "/" in _t_ques_sym:
        _t_symbol_pos = _find(_t_ques_sym, "/")
        ans = _sum([_t_ques_num[_t_symbol_pos], _t_ques_num[_t_symbol_pos + 1], "/"])
        _t_ques_num.pop(_t_symbol_pos)
        _num.pop(_t_symbol_pos + _addi_num)
        _t_ques_num.pop(_t_symbol_pos)
        _num.pop(_t_symbol_pos + _addi_num)
        _t_ques_sym.pop(_t_symbol_pos)
        _sym.pop(_t_symbol_pos + _addi_sym)
        _t_ques_num.insert(_t_symbol_pos, ans)
        _num.insert(_t_symbol_pos + _addi_num, ans)
    while "*" in _t_ques_sym:
        _t_symbol_pos = _find(_t_ques_sym, "*")
        ans = _sum([_t_ques_num[_t_symbol_pos], _t_ques_num[_t_symbol_pos + 1], "*"])
        _t_ques_num.pop(_t_symbol_pos)
        _num.pop(_t_symbol_pos + _addi_num)
        _t_ques_num.pop(_t_symbol_pos)
        _num.pop(_t_symbol_pos + _addi_num)
        _t_ques_sym.pop(_t_symbol_pos)
        _sym.pop(_t_symbol_pos + _addi_sym)
        _t_ques_num.insert(_t_symbol_pos, ans)
        _num.insert(_t_symbol_pos + _addi_num, ans)
    while "+" in _t_ques_sym:
        _t_symbol_pos = _find(_t_ques_sym, "+")
        ans = _sum([_t_ques_num[_t_symbol_pos], _t_ques_num[_t_symbol_pos + 1], "+"])
        _t_ques_num.pop(_t_symbol_pos)
        _num.pop(_t_symbol_pos + _addi_num)
        _t_ques_num.pop(_t_symbol_pos)
        _num.pop(_t_symbol_pos + _addi_num)
        _t_ques_sym.pop(_t_symbol_pos)
        _sym.pop(_t_symbol_pos + _addi_sym)
        _t_ques_num.insert(_t_symbol_pos, ans)
        _num.insert(_t_symbol_pos + _addi_num, ans)
    while "-" in _t_ques_sym:
        _t_symbol_pos = _find(_t_ques_sym, "-")
        ans = _sum([_t_ques_num[_t_symbol_pos], _t_ques_num[_t_symbol_pos + 1], "-"])
        _t_ques_num.pop(_t_symbol_pos)
        _num.pop(_t_symbol_pos + _addi_num)
        _t_ques_num.pop(_t_symbol_pos)
        _num.pop(_t_symbol_pos + _addi_num)
        _t_ques_sym.pop(_t_symbol_pos)
        _sym.pop(_t_symbol_pos + _addi_sym)
        _t_ques_num.insert(_t_symbol_pos, ans)
        _num.insert(_t_symbol_pos + _addi_num, ans)
print(ans)
