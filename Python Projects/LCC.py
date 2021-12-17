
"""m=int(input("Enter number of sources"))
a=[0 for i in range(m)]
for i in range(m):
    a[i]=int(input("Enter source "+str(i+1)+" :"))

n=int(input("Enter number of destinations"))
b=[0 for i in range(n)]
for i in range(n):
    b[i]=int(input("Enter destination "+str(i+1)+" :"))


x=[[0 for i in range(n)] for j in range(m)]
y=[[0 for i in range(n)] for j in range(m)]
z=[0 for i in range(m*n)]
z1=[0 for i in range(m*n)]
c=0

for i in range(m):
    for j in range(n):
        x[i][j]=int(input("Enter cost from source "+str(i+1)+" to destination "+str(j+1)+" : "))"""


m=3
n=4
a=[300,400,500]
b=[250,350,400,200]
x=[[3,1,7,4],[2,6,5,9],[8,3,3,2]]
y=[[0 for i in range(n)] for j in range(m)]
z=[0 for i in range(m*n)]
z1=[0 for i in range(m*n)]
c=0




for i in range(m):
    for j in range(n):
        z[c]=x[i][j]
        z1[c]=[i,j]
        c=c+1
        
###Sorting
for i in range(1, len(z)): 
  
        key = z[i]
        key1=z1[i]
        j = i-1
        while j >=0 and key < z[j] : 
                z[j+1] = z[j]
                z1[j+1]=z1[j]
                j -= 1
        z[j+1] = key
        z1[j+1] = key1

for i in z1:
    row=i[0]
    col=i[1]
    if a[row]>=b[col]:
        y[row][col]=b[col]
    else:
        y[row][col]=a[row]
    a[row]=a[row]-y[row][col]
    b[col]=b[col]-y[row][col]



for i in y:
    print(i)
for i in x:
    print(i)

c=0
for i in range(len(a)):
    for j in range(len(b)):
        c=c+x[i][j]*y[i][j]
print(c)

