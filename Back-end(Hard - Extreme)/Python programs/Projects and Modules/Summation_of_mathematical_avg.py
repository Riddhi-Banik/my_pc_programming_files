class Data:
    def __init__(self,_range_start,_range_end, value):
        if len(_range_start) == len(_range_end) == len(value):
            pass
        else:
            raise ValueError('Nope')
        self._range_start = _range_start
        self._range_end = _range_end
        self._range = []
        i = -1
        while True:
            i += 1
            self._range.append(f"{_range_start[i]}-{_range_end[i]}")
            if i == len(_range_start) - 1:
                break
        self.value = value
    def avg(self, ary:list):
        return sum(ary) / 2
    def range_mid(self):
        i = -1
        _mid = []
        while True:
            i += 1
            _mid.append(self.avg([self._range_end[i], self._range_start[i]]))
            if i == len(self._range_end) - 1:
                break
        return _mid
            
    
    def print_out(self):
        print('')
        i = -1
        while True:
            i += 1
            if i == len(self._range_start):
                break
            print(f"{self._range_start[i]} - {self._range_end[i]} | {self.value[i]}")
    def fixi(self):
        _mid = self.range_mid()
        _fixi = []
        i = -1
        while True:
            i += 1
            _fixi.append(self.value[i]*_mid[i])
            if i == len(self.value) - 1:
                break
        return _fixi
    def fixi_sum(self):
        _fixi = self.fixi()
        return sum(_fixi) / sum(self.value)
    
# not using input() to avoid timeouts
range_start = [20, 30, 40, 50, 60] # The start range of all fields arranged
range_end = [29, 39, 49, 59, 69] # The end range of all fields arranged
value = [10, 6, 18, 12, 8] # The value of all fields arranged
print('Splices: ' + str(len(value)) + ' ; ValueSum: ' + str(sum(value)))
data_point = Data(range_start, range_end, value)
data_point.print_out()
#ask = input("Summation?: ")
if True: #ask == str(1):
    print(f'\nMid : {data_point.range_mid()}')
    print(f'\nFixi : {data_point.fixi()} ; Fixi_sum: {sum(data_point.fixi())}')
    print(f'\nSummation : {data_point.fixi_sum():.4f}')
