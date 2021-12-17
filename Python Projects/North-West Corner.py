"""m=int(input("Enter number of sources"))
a=[0 for i in range(m)]
for i in range(m):
    a[i]=int(input("Enter source "+str(i+1)+" :"))
print(a)    
n=int(input("Enter number of destinations"))
b=[0 for i in range(n)]
for i in range(n):
    b[i]=int(input("Enter destination "+str(i+1)+" :"))
print(b)
x=[[0 for i in range(n)] for j in range(m)]
y=[[0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        x[i][j]=int(input("Enter cost from source "+str(i+1)+" to destination "+str(j+1)+" : "))"""


m=3
n=4
a=[300,400,500]
b=[250,350,400,200]
x=[[3,1,7,4],[2,6,5,9],[8,3,3,2]]
y=[[0 for i in range(n)] for j in range(m)]
flag=0
while flag==0:
    row=a.count(0)
    col=b.count(0)
    if a[row]>=b[col]:
        y[row][col]=b[col]
    else:
        y[row][col]=a[row]
    a[row]=a[row]-y[row][col]
    b[col]=b[col]-y[row][col]
    flag=1
    for i in range(m):
        if a[i]!=0:
            flag=0


for i in y:
    print(i)
for i in x:
    print(i)


c=0
for i in range(len(a)):
    for j in range(len(b)):
        c=c+x[i][j]*y[i][j]
print(c)
        
    
    
    
    
