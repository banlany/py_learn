def move(i,fr,to):
    n=0
    str1 = " "
    str1 += str(i) +" "+str(fr)+" -> "+str(to)
    print(str1,end="")
    if fr == 'A':
        listA.pop()
    elif fr == 'B':
        listB.pop()
    elif fr == 'C':
        listC.pop()
    if to == 'A':
        if len(listA) >= 1:
            n = listA[len(listA)-1]
        listA.append(i)
        
    elif to == 'B':
        if len(listB) >= 1:
            n = listB[len(listB)-1]
        listB.append(i)
        
    elif to == 'C':
        if len(listC) >= 1:
            n = listC[len(listC)-1]
        listC.append(i)
        
    if n%2==i%2 and n!=0 :
        print(" wrong")
    else:
        print(" right")
    
def honno_move(l,fr,via,to):
    if l == 1:
        move(l,fr,to)
    else:
        honno_move(l-1,fr,to,via)
        move(l,fr,to)
        honno_move(l-1,via,fr,to)

listA= []
listB= []
listC= []

n = int(input("hanon: "))
for i in range(n):
    listA.append(i+1)
honno_move(n,'A','B','C')





