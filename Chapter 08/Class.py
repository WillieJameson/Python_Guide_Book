"""count_from_by() is a function call, whereas CountFromBy() creates an object"""
class CountFromBy:
  def __init__(self, v: int=0 , i: int=1) -> None:
    self.val = v
    self.incr = i
  def increase(self) -> None :
    self.val += self.incr
  def __repr__(self) -> str:
      return str(self.val)

k = CountFromBy()
k
# expected output = 0
k.increase()
k
# expected output = 1
print(k)
# expected output = 1
i = CountFromBy(100)
i
# expected output = 100
i.increase()
print(i)
# expected output = 101

m = CountFromBy(100,10)
m
# expected output = 100
m.increase()
m
# expected output = 110
n = CountFromBy(i=15)
n
# expected output = 0
n.increase()
n
# expected output = 15

