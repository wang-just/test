#encoding=utf-8
import os
import sys
path=r'C:\Users\danny\pythonProgram\LP4E-examples'
files=os.listdir(path)

for name in files:
    a=os.path.splitext(name)
    if a[1]=='.txt':
        newname=a[0]+'.py'
        print(name+' '+newname)
        os.chdir(path)
        os.rename(name,newname)
