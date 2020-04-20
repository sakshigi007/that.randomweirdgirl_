N=int(input(" length of the list:"))

a=[]
b=[]

print("Enter the predefined order to be printed.")
for i in range(N):
    b.append(int(input()))
    
print("Enter the strings to be printed.")
for i in range(N):
    a.append(input())


def print_string(N,a,b):
    for i in range(N):
        if b[i]==min(b):
            if b[i]==i+1:
                print(a[i])
            else:
                if len(a[i])==b[i]:
                    print(a[i].upper())
                else:
                    print(a[i].lower())
            return i
            break
            
            
for i in range(N):
    p=print_string(N,a,b)
    b[p]=N+1