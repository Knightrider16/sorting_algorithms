def merge_sort(list1):
    if(len(list1)>1):
        mid=len(list1)//2
        left_part=list1[:mid]
        right_part=list1[mid:]

        merge_sort(left_part)
        merge_sort(right_part)

        i=j=k=0

        while((i<len(left_part)) and (j<len(right_part))):
            if left_part[i]<=right_part[j]:
                list1[k]=left_part[i]
                i+=1
            else:
                list1[k]=right_part[j]
                j+=1
            k+=1

        while((i<len(left_part))):
            list1[k]=left_part[i]
            i+=1
            k+=1

        while((j<len(right_part))):
            list1[k]=right_part[j]
            j+=1
            k+=1

list1=[]
n=int(input("Enter how many elements needed"))
for i in range(n):
    list1.append(int(input("Enter an element")))
merge_sort(list1)
print(list1)