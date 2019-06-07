string=input("Name the month: ")
list1=['January','March','May','July','August','October','December']
list2=['April','June','August','September','November']
list3=['February']
for i in range(0,7):
    if string==list1[i]:
        print("31")
for i in range(0,5):
    if string==list2[i]:
        print("30")
if string==list3[0]:
    print("28,if not  a leap year")
    print("29,if a leap year")
