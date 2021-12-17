
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

c=[]
d=[]
e=[]
f=[]
for i in range(m):
    for j in range(n):
        x[i][j]=int(input("Enter cost from source "+str(i+1)+" to destination "+str(j+1)+" : "))"""
    

m=3
n=4
a=[300,400,500]
b=[250,350,400,200]
x=[[3,1,7,4],[2,6,5,9],[8,3,3,2]]
y=[[0 for i in range(n)] for j in range(m)]
c=[]
d=[]
e=[]
f=[]



for i in range(m+n):
    c=[]
    d=[]
    ###row with non_zeros
    for j in range(m):
        if a[j]!=0:
            c.append(j)
    
    ###col with non_zeros
    for j in range(n):
        if b[j]!=0:
            d.append(j)
    
    if len(c)==0:
        break

    elif len(c)==1:
        for j in d:
            y[c[0]][j]=b[j]
            a[c[0]]=a[c[0]]-y[c[0]][j]
            b[j]=b[j]-y[c[0]][j]

    elif len(d)==1:
        for j in c:
            y[j][d[0]]=a[j]
            a[j]=a[j]-y[j][d[0]]
            b[d[0]]=b[d[0]]-y[j][d[0]]

    else: 
        e=[]
        ###row penalties
        for j in c:
            z=[]
            
            for k in d:
                z.append(x[j][k])
            z.sort()
            
            e.append(z[1]-z[0])
            
        
        f=[]
        
        for j in d:
            z=[]
            
            for k in c:
                z.append(x[k][j])
            z.sort()
            f.append(z[1]-z[0])
       

        if max(e)>max(f):
            ma=max(e)
            
            e=c[e.index(ma)]
            
            f=[]
            for j in d:
                f.append(x[e][j])
            f=f.index(min(f))
            f=d[f]
            if a[e]<b[f]:
                y[e][f]=a[e]
            else:
                y[e][f]=b[f]
            a[e]=a[e]-y[e][f]
            b[f]=b[f]-y[e][f]
        else:
            ma=max(f)
            
            f=d[f.index(ma)]
            
            e=[]
            for j in c:
                e.append(x[j][f])
            e=e.index(min(e))
            e=c[e]
            if a[e]<b[f]:
                y[e][f]=a[e]
            else:
                y[e][f]=b[f]
            a[e]=a[e]-y[e][f]
            b[f]=b[f]-y[e][f]
        


    
        
            
        
        
    
    
    
    

    
for i in y:
    print(i)

for i in x:
    print(i)
c=0
for i in range(len(a)):
    for j in range(len(b)):
        c=c+x[i][j]*y[i][j]
print(c)

