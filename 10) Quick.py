def entries(a):
    n=int(input("Enter Number of student:"))
    for i in range(n):
        m=float(input("Enter percentage of student:"))
        a.append(m)
    print("Array Entries are Recorded\n\n")

def display(a):
    n=len(a)
    if n==0:
        print("No records entered\n")
    else:
        print("Array of percentage:  ",end='  ')
        for i in range(len(a)):
            print(a[i],end='  ')
    print("\n")

def partition(a,f,l):
    pivot=a[f]
    left=f+1
    right=l
    while True:
        while left<=right and a[left]<=pivot:
            left=left+1
        while left<=right and a[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            a[left],a[right]=a[right],a[left]
    a[f],a[right]=a[right],a[f]
    return right

def quick_sort(a,f,l):
    if f<l:
        p=partition(a,f,l)
        quick_sort(a,f,p-1)
        quick_sort(a,p+1,l)



a=[]
while True:
    print("sort by quicksort")
    entries(a)
    display(a)
    print("\n")
    print("Percentage before sorting\n")
    display(a)
    print("Percentages after sorting\n")
    n=len(a)
    quick_sort(a,0,n-1)
    display(a)
    if n>=5:
            print("------------Top five scores----------\n")
            for i in range(n-1,n-6,-1):
                print(a[i],"\n")
    else:
            print("----------Top scores-----------\n")
            for j in range(n-1,-1,-1):
                print(a[j],"\n")
