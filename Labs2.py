#ЗАДАНИЕ_1
a= True
b= False
x=1
print(x, a and b)
x=2
print(x, (a and b) or b)
x=3
print(x, (a and b) or not( a and b))
x=4
print(x, (a and b) or not( a or b) or b)
x=5
print(x, b and b or not a and (a or b or a) or not (a or b))
x=6
print(x, 1<<2)
x=7
print(x, 1 & 0 | 1 >> 1)
x=8
print(x, 1 & 0 | 1 >> 0)
x=9
print(x, 0b101 & 0b111 ^ 0b111 | 0b010)

#ЗАДАНИЕ_2
x_ = int(input('Enter number X: '))
y_ = int(input('Enter number Y: '))
if x_< y_:
    print(f'{x_} is smaller than {y_}')
elif x_ == y_:
    print(f'{x_} is equal to {y_}')
else:
    print(f'{y_} is smaller than {x_}')

#ЗАДАНИЕ_3
x_ = int(input('Enter number X: '))
y_ = int(input('Enter number Y: '))
z_ = int(input('Enter number Z: '))
def Largest_number (a,b,c):
    maximum_ = max(a,b,c)
    return maximum_
if x_ == y_ == z_:
    print('The numbers inputed are equal')
else:
    conc = Largest_number(x_, y_, z_)
    print(conc, 'is the largest number')

#ЗАДАНИЕ_4
x_ = int(input('Enter number X: '))
y_ = int(input('Enter number Y: '))
z_ = int(input('Enter number Z: '))
list1 = [x_,y_,z_]
unique_list = []
for i in list1:
    if i not in unique_list:
        unique_list.append(i)
print(f'There exists {len(unique_list)} unique numbers in {(x_,y_,z_)}={unique_list}')