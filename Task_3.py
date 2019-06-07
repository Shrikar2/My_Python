num=int(input("Enter number of words:" ))
list2=['a']
list2.pop()
for i in range(0,num):
    list2.append(input())
for i in range(0,num-1):
    a=len(list2[i])
    b=len(list2[i+1])
    if a>b:
        max1=a
    else:
        max1=b
print(max1)
