# Question 2

def sort():
    num = int(input("請輸入n值(0-100) :  "))

    list = []
    check_3 = 0
    
    for count in range(num):
        list.append(count + 1)

    while True:
        if len(list) == 1:
            print('為第', list[0], '順位')
            break
        else:
            check_3 = check_3 + 1
            get = list[0]
            list.pop(0)
            if check_3 == 3:
                check_3 = 0
                continue
            else:
                list.append(get)
                continue

sort()

