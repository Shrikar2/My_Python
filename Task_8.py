Sample_List=[8, 2, 3, -1, 7]
for i in range(0,4):
     Sample_List[i+1]=Sample_List[i] * Sample_List[i+1]
     Value=Sample_List[i+1]
print(Value)
