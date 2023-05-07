# Question 1

def triangle():
    num = int(input("請輸入整數 :  "))
    for count in range(1, num):
        print(' ' * (num - count), end = '')
        print('*', end = '')
        if count == 1:
            print('')
        else:
            print(' ' * (2*(count-1)-1), end = '')
            print('*')
    print('* '* num)

triangle()

