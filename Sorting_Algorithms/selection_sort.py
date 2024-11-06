def selection(count,list1):
    if(count>=len(list1)-1):
        return
    min=count
    for i in range(count,len(list1)):
        if(list1[i]<list1[min]):
            min=i
    list1[min],list1[count]=list1[count],list1[min]
    selection(count+1,list1)

list1=[]
count=0
n=int(input("Enter how many elements needed"))
for i in range(n):
    list1.append(int(input("Enter an element")))
selection(count,list1)
print(list1)
