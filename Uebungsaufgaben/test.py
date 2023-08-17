import numpy as np

for i in range(10,30):
    num1= i^3
    num2 =i^4
    if 1000<num1<10000:
        continue
    else:
        if 100000<num2<1000000:
            continue
        else:
            num1 = i ^ 3
            num2 = i ^ 4
            num1_Array = list(map(int, str(num1)))
            num2_Array = list(map(int, str(num2)))
            if len(set(num1_Array) ^ set(num2_Array)) == len(num1_Array) + len(num2_Array):
                n = i
                break

print('This is the Number we want {}'.format(n))


