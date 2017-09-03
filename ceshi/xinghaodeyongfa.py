#coding:utf-8
def add(*args):
    s=sum(args)
    return s
a=(1,2,3,4,5)
print add(*a)
b=[1,2,3,4,5,6,7]
print add(*b)