a=list(open(r'C:\Users\danny\test.txt'))
for x in a:print(x.rstrip(),end='')
a=open(r'C:\Users\danny\test.txt')
for line in a:
    print(line,sep=' ',end='')
a.seek(0)
b=[lin.rstrip() for lin in a]
for i in b:
    print(i)
a.seek(0)
c=[line.rstrip() for line in list(a)]
print (c)
print(list(map(ord,'spam')))
S='spam'
for (offset,item) in enumerate(S):
    print(offset,item)
print(list([c*i for(i,c) in enumerate(S)]))
E=enumerate(S)
print(E.__next__())

    