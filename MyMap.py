import time
def myMap(func,*seqs):
    res=[]
    start=time.clock()
    for args in zip(*seqs):
        res.append(func(*args))
    end=time.clock()-start
    print(end)
    return res
def myMap2(func, *seqs):
    return [func(*x) for x in zip(*seqs)]
def myMap3(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)
def myMap4(func,*seqs):
    return (func(*x) for x in zip(*seqs))

def timesfour(S):
    for c in S:
        yield c * 4

G = timesfour('spam')# Generator functions work the same way
print('-'*3)
print(iter(G) is G)
print(myMap(abs,[-2,-1,0,1,2]))
print(myMap2(abs,[-2,-1,0,1,2]))
print(myMap3(abs,[-2,-1,0,1,2]))
my=myMap4(abs,[-2,-1,0,1,2])

print(next(my))