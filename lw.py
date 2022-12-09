file = open('lw.txt', 'r')

check = int(input('Input number in format XXX: \n'))
print('The time value at which the measurement results exceed the value entered by the user:')
 
for i in file:
    x = i.find(' ') + 1
    num = ''
    for n in range(x, len(i)-1):
        num += i[n]
    if int(num) > check:
        print(i[0:5])