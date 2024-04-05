import RDHI_AdvCustomModule as _math
import math

_ques = input("Insert a mathematical question: ")
#_ques = "pi * 8^2"
_ques = _ques.strip()
#rdhi functions
_ques = _ques.replace("gcf", "_math.gcf_value_int")
_ques = _ques.replace("lcm", "_math.lcm_value_int")
_ques = _ques.replace("^","**")
#constants
_ques = _ques.replace("pi","(math.pi + 0)")
_ques = _ques.replace("e","(math.e + 0)")
_ques = _ques.replace("tau","math.tau")
#mathmetical_functions
_ques = _ques.replace("radCos","math.cos")
_ques = _ques.replace("radSin","math.sin")
_ques = _ques.replace("exp","math.exp")
_ques = _ques.replace('%','* 0.01')
_res = 0.0
try:
    _res.write("input_bar",eval(_ques))
except:
    print("Error")