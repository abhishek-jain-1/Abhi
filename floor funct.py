import math
x = 1
total = 0
for x in range(0,2020):
    x = x**1/2
    x = math.floor(x)
    total = total + x
print (total)
