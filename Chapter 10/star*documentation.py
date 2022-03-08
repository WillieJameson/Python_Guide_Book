# * as meaning “expand to a list of values.”

def myfunc(*args):
  for a in args:
    print(a, end=' ')
  if args:
    print()

# myfunc(10)
# 10
# myfunc()
# """does nothing"""
# myfunc(10,20,30,40,50,60,70)
# 10 20 30 40 50 60 70
# myfunc(1,'two', 3,'four', 5, 'six',7)
# 1 two 3 four 5 six 7
# values = [1,2,3,5,7]
# myfunc(values)
# [1,2,3,5,7]
# myfunc(*values)
# 1 2 3 5 7 

# kwargs is for key and value / dict
def myfunc2(**kwargs):
  for k,v in kwargs.items():
    print(k,v, sep ='->', end ='')
  if kwargs:
    print()

# myfunc2(a=10,b=20)
# b->20 a->10
# myfunc2()
# """does nothing"""
# myfunc2(a=10,b=20,c=30,d=40,e=50,f=60)
# b->20 f->60 d->40 c->30 e->50 a->10

def myfunc3(*args, **kwargs):
  if args:
    for a in args:
      print(a, end=' ')
    print()
  if kwargs:
    for k,v in kwargs.items():
      print(k,v, sep ='->', end ='')
    print()

# myfunc3()
# myfunc3(1,2,3)
# 1 2 3 
# myfunc3(a =10, b=20, c =30)
# a->10 b->20 c->30
# myfunc3(1,2,3,a=10,b=20,c=30)
# 1 2 3 
# a->10 b->20 c->30