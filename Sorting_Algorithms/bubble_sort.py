def bubble_sort(list1,length):
    if length<=1:
        return
    for i in range(0,length-1):
        if(list1[i]>list1[i+1]):
            list1[i],list1[i+1]=list1[i+1],list1[i]
    bubble_sort(list1, length - 1)

list1=[]
n=int(input("Enter how many elements needed"))
for i in range(n):
    list1.append(int(input("Enter an element")))
length=len(list1)
bubble_sort(list1,length)
print(list1)
