n = input("Enter a number: ")

def left_num(num):
    if num == 0:
        return 0
    else:
        c = 0
        k = num//2
        for i in range(1,k+1):
            c += left_num(i)
            if i // 10 >0:
                if i%10//2 >= i//10:
                    c -= left_num(i%10)
        return c+1
print(left_num(int(n)))