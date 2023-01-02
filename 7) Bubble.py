L=[]
def get():
    n=int(input("Enter Number of First Year Students: "))
    for i in range(n):
        no=int(input("Enter their Percentage: "))
        L.append(no)
def dis():
    for i in L:
        print(i,end=" ")
def bubble():
    cnt=1
    for i in range(len(L)-1,0,-1):
        for j in range(0,i):
            if(L[j]>L[j+1]):
                L[j], L[j + 1] = L[j + 1], L[j]
                print(L)
        cnt+=1
    j=-1
    print("\n****Top five scores****=")
    while(j!=-6):
        print(L[j],end=" ")
        j=j-1

if __name__ == '__main__':
    while(1):
        print("Bubble Sort")
        get()
        print("****Displaying List****")
        dis()
        bubble()
