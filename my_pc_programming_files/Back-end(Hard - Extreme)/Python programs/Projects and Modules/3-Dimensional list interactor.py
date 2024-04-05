import math

def num_filter(number):
    number = str(number)
    _num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    res = ""
    for x in number:
        if x in _num:
            res += x
    res = str(res)
    return res

third__dimension = [    #1 = y, 2 = x, 3 = z
                      [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]],
                      [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]],
                      [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
                   ]

print("1st list = Y, 2nd list = X, 3rd list = Z 4th list(comming  soon, block id) = T")

Random_num = input("insert a seed(int): ")+"0" # 1096 (random)
Random_num = num_filter(Random_num)
Random_num = int(Random_num)
R_str = str(Random_num)
#processing
#randomizer
if Random_num == 0:
    Random_num = 1111
else:
    pass
R_I = int(R_str[-1])
R_II = int(R_str[-1])
Random_num = (R_I * R_II + 56 - 32) * Random_num
Random_num = str(Random_num)
Random_num  = Random_num[1]
Random_num = int(Random_num)
if Random_num > 5:
    Random_num /= 2
else:
    pass
Random_num = math.floor(Random_num + 0.3 )
if Random_num == 0:
    Random_num = 1
else:
    pass
    
#randomizer
#--------------------------
#seed-applier
y_co = 0
x_co = 0
z_co = 0

for Y in third__dimension:
    for X in Y:
        for Z in X:
            Random_num = str(Random_num)
            third__dimension[y_co][x_co][z_co] = Random_num
            third__dimension[y_co][x_co][z_co] = third__dimension[y_co][x_co][z_co]
            z_co += 1
        x_co += 1
        z_co = 0
    y_co += 1
    x_co = 0
    z_co = 0
#seed-applier
#processing





#results▼
print(' ')
print(Random_num)
print(third__dimension[0])
print(third__dimension[1])
print(third__dimension[2])