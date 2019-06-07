print("Enter the lengths of three sides of a triangle:" )
side_1=input("Enter the length of first side: ")
side_2=input("Enter the length of second side: ")
side_3=input("Enter the length of third side: ")
if side_1==side_2 and side_2==side_3 and side_1==side_3:
    print("Equilateral")
elif side_1!=side_2 and side_2!=side_3 and side_1!=side_3 :
    print("Scalene")
elif side_1==side_2 or side_2==side_3 or side_1==side_3:
    print("Isoceles")
