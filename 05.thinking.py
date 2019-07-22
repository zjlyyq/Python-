import time
str = ''
for i in range(0,1000000):
    str += '1'

start_time = time.perf_counter()
s = " "
for n in range(0,1000000):
    s += str[n]

end_time = time.perf_counter()

print('脚本一时间消耗：{}'.format(end_time-start_time))

start_time = time.perf_counter()

s = " "
l = []
for n in range(0,1000000):
    l.append(str[n])
s = ' '.join(l)

end_time = time.perf_counter()

print('脚本二时间消耗：{}'.format(end_time-start_time))