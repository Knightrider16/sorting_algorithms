def quick_sort(list1):
    if(len(list1)>1):
        pivot=list1[-1]
        k=0
        i=0
        while(i<len(list1)-1):
            if(list1[i]<pivot):
                list1[k],list1[i]=list1[i],list1[k]
                k+=1
            i+=1
        list1[k],list1[-1]=list1[-1],list1[k]
        left=list1[:k]
        right=list1[k+1:]

        quick_sort(left)
        quick_sort(right)
        list1[:]=left+[list1[k]]+right

list1=[]
n=int(input("Enter how many elements needed"))
for i in range(n):
    list1.append(int(input("Enter an element")))
quick_sort(list1)
print(list1)