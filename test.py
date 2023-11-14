#%%
def count_tax(income):
    if income <= 60000:
        tax = 0
    elif income <= 100000:
        tax = (income - 60000) * 0.03
    elif income <= 180000:
        tax = 1200 + (income - 100000) * 0.10
    elif income <= 300000:
        tax = 1200 + 8000 + (income - 180000) * 0.18
    elif income <= 480000:
        tax = 1200 + 8000 + 21600 + (income - 300000) * 0.25
    elif income <= 700000:
        tax = 1200 + 8000 + 21600 + 45000 + (income - 480000) * 0.30
    elif income <= 1000000:
        tax = 1200 + 8000 + 21600 + 45000 + 66000 + (income - 700000) * 0.35
    else:
        tax = 1200 + 8000 + 21600 + 45000 + 66000 + 105000 + (income - 1000000) * 0.45

    return tax
income = float(input())
tax = count_tax(income)
print(f"{tax:.2f}")
#%%
def num_link(a,b):
    a = str(a)
    b = str(b)
    len_c = len(a)+len(b)
    c = ''
    ca = 0
    cb = 0
    for i in range(len_c):
        if ca < len(a):
            c += a[ca]
            ca += 1
        if cb < len(b):
            c += b[cb]
            cb += 1
    return int(c)
a,b= map(int,input().split())
print(num_link(a,b))
# %%
n = int(input())
a = []
for i in range(2,n+1):
    flag = 0
    for j in range(2,i//2+1):
        if i%j == 0:
            flag = 1
    if flag == 0:
        a.append(i);
for i in range(len(a)):
    if i != len(a)-1:
        print(a[i],end=' ')
    else:
        print(a[i],end='')

# %%

N = int(input().strip())  
scores = list(map(int, input().strip().split()))  
average = sum(scores) / N  
count = len([score for score in scores if score >= 60])  
print("average = {:.1f}".format(average))  
print("count = {}".format(count))  
# %%
n = int(input().strip())
dic = {}
for i in range(n):
    c,d = input().split()
    dic[d] = c
line = str(input().strip())
while line != "dog":
    if line in dic:
        print(dic[line])
    else:
        print("dog")
    line = str(input().strip())
#%%
def print_sorted_set(s):  
    # 定义一个函数，参数为s，返回一个排序后的字符串
    print(' '.join(map(str, sorted(s))))
  
n = int(input())  
A = set(map(int, input().split()))  
  
m = int(input())  
B = set(map(int, input().split()))  
  
intersection = A & B  
union = A | B  
difference = A - B  

print_sorted_set(intersection)  
print_sorted_set(union)  
print_sorted_set(difference)
#%%
def LRU(n,visit):
    count = 0
    buffer = []
    for i in range(len(visit)):
        if i < n:
           buffer.append(visit[i])
           count += 1
        else:
            if visit[i] in buffer:
                buffer.remove(visit[i])
                buffer.append(visit[i])
            else:  
                buffer.remove(buffer[0])
                buffer.append(visit[i])
                count += 1
    print(count)
    buffer.sort()
    print(' '.join(map(str, buffer)))
    
n,m = map(int,input().split())
visit = list(map(int,input().split()))
LRU(n,visit)
# %%
def LRU(n,visit):
    count = 0
    buffer = []
    for i in range(len(visit)):
        if  visit[i] in buffer:
            buffer.remove(visit[i])
            buffer.append(visit[i])
           
        else:
            if i < n:
                buffer.append(visit[i])
                count += 1
            else:  
                if len(buffer) < n:
                    buffer.append(visit[i])
                    count += 1
                else:
                    buffer.pop(0)
                    buffer.append(visit[i])
                    count += 1
    print(count)
    buffer.sort()
    print(' '.join(map(str, buffer)))
    
n,m = map(int,input().split())
visit = list(map(int,input().split()))
LRU(n,visit)
#%%
def insert_sort(nums):  
    for i in range(1, len(nums)):  
        key = nums[i]  
        j = i - 1  
        while j >= 0 and key < nums[j]:  
            nums[j + 1] = nums[j]  
            j -= 1  
        nums[j + 1] = key  
        print(' '.join(map(str, nums)))  
  
n = int(input())  
nums = list(map(int, input().split()))  
insert_sort(nums)
#%%
string = input()
print(''.join(sorted(set(string))))

# %%
n,m  = map(int,input().split())
matrix1 = str(input())
matrix1 = matrix1.replace('[','')
matrix1 = matrix1.replace(']','')
matrix1 = list(matrix1.split(','))
matrix2 = str(input())
matrix2 = matrix2.replace('[','')
matrix2 = matrix2.replace(']','')
matrix2 = list(matrix2.split(','))
addmatrix = []
i = 0
for j in range(n):
    
    temp = []
    for k in range(m):
        temp.append(int(matrix1[i])+int(matrix2[i]))
        i+=1
    addmatrix.append(temp)
str1 = ""
str1 += str(addmatrix)
print(str1.replace(' ',''))
#%%
n = int(input())
stack = list(map(int, input().split()))
out_stack = []
line = str(input())
op,*args = line.split()
if op == 'push':
    for i in range(len(args)):
        stack.append(int(args[i]))
elif op == 'pop':
    for i in range(int(args[0])):
        if len(stack) > 0:
          out_stack.append(stack.pop())
line = str(input())
op,*args = line.split()
if op == 'push':
    for i in range(len(args)):
        stack.append(int(args[i]))
elif op == 'pop':
    for i in range(int(args[0])):
        if len(stack) > 0:
          out_stack.append(stack.pop())
str1 = str(stack).replace("[","")
str1 = str1.replace("]","")
str1 = str1.replace(",","")
str2 = str(out_stack).replace("[","")
str2 = str2.replace("]","")
str2 = str2.replace(",","")
if len(stack) > 0:
    print("len = "+ str(len(stack))+", data = "+str1 )
else:
    print("len = "+ str(len(stack)))
if len(out_stack) > 0:
    print("len = "+ str(len(out_stack))+", data = "+str2 )
else:
    print("len = "+ str(len(out_stack)))
#%%
