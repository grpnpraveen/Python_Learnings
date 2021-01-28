def selection(a,size):
    for i in range(size-1):
        min=i
        for j in range(i+1,size):
            if a[j]<a[min]:
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
a=[1,2,4,3]
selection(a,4)


for i in range(4):
    print(a[i])
