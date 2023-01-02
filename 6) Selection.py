L=[]
def get():
    n=int(input("Enter Number of First Year Students: "))
    for i in range(n):
        no=int(input("Enter their Percentage: "))
        L.append(no)
def dis():
    for i in L:
        print(i,end=" ")

def sel():
    for i in range(len(L)):
        min=i
        print("\nIteration No:",i)
        for j in range(i+1,len(L)):
            if L[j]<L[min]:
                min=j
        L[i],L[min]=L[min],L[i]
        print(L,end="\n")

    j = -1  # [1,2,3,4]  #index=(0,1,2,3)-> forward index  #(-4,-3,-2,-1)
    print("\n****Top five scores****=")
    while (j !=-6):
        print(L[j],end=" ")
        j = j - 1

if __name__ == '__main__':
    while(1):
        print("Selection Sort")
        get()
        print("****Displaying List****")
        dis()
        sel()
