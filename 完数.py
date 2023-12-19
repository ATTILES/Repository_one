n=int(input())
for i in range(1,n):
    sum=0
    ls=[]
    for j in range(1,i):
        if i%j==0:
            ls.append(j)
            sum+=j
    if sum==i:
        print("{} its factors are".format(i),*ls)
