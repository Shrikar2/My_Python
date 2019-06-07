odd_count=0
even_count=0
Numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0,9):
    if Numbers[i]%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Number of even numbers: ",even_count)
print("Number of odd  numbers: ",odd_count)
