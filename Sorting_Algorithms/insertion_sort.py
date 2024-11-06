def insertion_sort(list1):
    for j in range(1,len(list1)):
        for i in range(j,0,-1):
            if(list1[i]<list1[i-1]):
                list1[i],list1[i-1]=list1[i-1],list1[i]
            else:
                break

list1=[]
n=int(input("Enter how many elements needed"))
for i in range(n):
    list1.append(int(input("Enter an element")))
insertion_sort(list1)
print(list1)