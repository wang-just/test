#encoding=utf-8
import sys
#file=open(r'C:\Users\danny\test.txt','w')
#file.write('ssss')
#file.close()
#del file

a={}
a[(2,3,4)]='王超'
a.update(name= 'wc',age= 22)#合并两个字典
value={'name':'wc','age': 22}
print(value)
v=dict(name='wc',age=22)
print(v)
print(a)
b=a.pop('name')
print(a)
sys.stdout.write(b+'\n')
i=10
while i:
    i -= 1
    sys.stdout.write(str(i))
else:
    sys.stdout.write(str(i))