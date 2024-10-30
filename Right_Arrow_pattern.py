n=int(input())
for i in range(n): 
    j=0
    while j<=(i):
        print("*",end=" ")
        j+=1
    print()
for i in range(n-1,-1,-1):
    j=0
    while j<i:
        print("*",end=" ")
        j+=1
    print()
