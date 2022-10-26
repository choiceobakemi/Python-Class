1)

sum_ = 0
 for i in range(10):
    
    t_ = int(input('input number : '))
    sum_ = sum_ + t_
 print(sum_) 

2)
zeros_ = []
for i in range(5):
    s_ = int(input('enter number: '))
    if s_ == 0:
        zeros_.append(s_)
if len(zeros_) == 0:
    print("массив чисел не включает нуль")
else:
    print(f'в массивах чисел есть {len(zeros_)} нули')

 3)
n_ = int(input('введите натуральное число'))
for i in range(n_):
    list_ = list(range(1,i +2))
    print(*list_, sep= '')

        #Или
n_ = int(input('введите натуральное число'))
for i in range(n_):
    
    print(*range(1,i+2), sep='')

 4)
n_ = int(input('введите натуральное число: '))
for i in range(n_):
    tb = list(range(1,i+1))
    t_ = sorted(tb,reverse=True)
    for j in range(n_-i-1):
        print(' ', end='')
    print(*range(1,i+2), sep='', *t_)
