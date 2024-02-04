divider = [2]
# comments are declared by (#). They do not affect the code. It also can be saved. 

def elementary_numbers(): # declare "divider = [2]"
    global divider
    limit = 10
    limit_perm = limit
    fu_number = 2
    divider = [2]
    recorder = []
    will_break = 0

    while limit > 0:
        will_break = 0

        for x in divider:
            
            if will_break == 0:

                recorder = []
                if fu_number / x in range(limit_perm):
                    recorder.append("0") # non-fundamental or have installed.
                elif fu_number / x not in range(limit_perm):
                    recorder.append("1") # fundamental.

                if "0" in recorder:
                    fu_number += 1
                    limit -= 1
                elif "1" in recorder:
                    divider.append(fu_number)
                    fu_number += 1
                    limit -= 1
                    will_break = 1
                

    return divider
    

divider = elementary_numbers()
print(divider)
    
    
