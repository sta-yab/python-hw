# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

f = open("lesson55.txt",'w')
res = 0
for i in range(1,10):
    n = random.randint(1,10)
    f.write(str(n)+' ')
    res += n
print (res)
