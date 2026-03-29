# 1. int()
print(int('42'), int(3.9), int('1010', 2))

# 2. float()
print(float('3.14'), float(5))

# 3. str()
print('Score: ' + str(100))
print(str([1,2,3]))

# 4. bool()
print(bool(0), bool(42), bool(''), bool('hello'))

# 5. list()
print(list((1,2,3)))
print(list("hello"))

# 6. tuple()
print(tuple([10,20,30]))

# 7. set()
print(set([1,2,2,3,4]))

# 8. dict()
print(dict(name='Ali', age=20))
print(dict([('x',1),('y',2)]))

# 9. complex()
c = complex(3,4)
print(c, c.real, c.imag)

# 10. bytes()
print(bytes(5))
print(bytes([65,66,67])) # it prints the b'ABC

# 11. abs()
print(abs(-15), abs(-3.14))

# 12. round()
print(round(3.14159,2), round(2.5))

# 13. pow()
print(pow(2,10), pow(2,10,1000))

# 14. max()
print(max([5,2,9,1]))

# 15. min()
print(min([5,2,9,1]))

# 16. sum()
print(sum([10,20,30]))

# 17. divmod()
print(divmod(17,5))

# 18. hash()
print(hash("python"))

# 19. hex()
print(hex(255))

# 20. oct()
print(oct(64))

# 21. bin()
print(bin(10))

# 22. chr()
print(chr(65))

# 23. ord()
print(ord('A'))
print([ord(c) for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])

# 24. format()
print(format(3.14159, '.2f'))

# 25. repr()
s = 'hello\nworld'
print(repr(s))

# 26. input() (simulated)
name = "Shamshuddin"
print("Hello", name)

# 27. print()
print("Hello", "World")

# 28. range()
print(list(range(5)))

# 29. len()
print(len("python"))

# 30. enumerate()
for i, j in enumerate(['a','b','c']):
    print(i, j)

# 31. zip()
print(list(zip([1,2], ['a','b'])))
print(dict(zip({'name','age'},{'raju',34})))

# 38. zip (unzip)
pairs = [(1,'a'),(2,'b')]
nums, chars = zip(*pairs)
print(nums, chars)

# 32. map()
print(list(map(lambda x:x*x, [1,2,3])))

# 33. filter()
print(list(filter(lambda x:x%2==0, [1,2,3,4])))

# 34. sorted()
print(sorted([5,2,9]))

# 35. reversed()
print(list(reversed([1,2,3])))

# 36. any() : Checks if at least one value is True [0 = false,1 = true,0 = false]
print(any([0,1,0]))

# 37. all() : Checks if all values are True                [0 = false,1 = true,0 = false] it return false
print(all([1,2,3]))

# 39. type()
print(type(10))

# 40. isinstance()
print(isinstance(10, int))

# 41. issubclass()
class A: pass
class B(A): pass
print(issubclass(B, A))

# 42. id()
a = [1,2]
b = a
print(id(a) == id(b))

# 43. dir()
print(dir([])[:5])

# 44. vars() : Return __dict__ of object. Used to inspect object attributes, dynamic attribute access
class P:
    def __init__(self):
        self.x = 1
p = P()
print(vars(p))

# 45. help()
# In interpreter: help(len)
# Prints full docs
# Simulated:

print(len.__doc__[:30])

# 46. callable()
def f(): pass
print(callable(f), callable(10))

# 47. hasattr()
class Car:
    speed = 100
c = Car()
print(hasattr(c, 'speed'))
print(hasattr(c, 'color'))


# 48. getattr()
class Person:
name = 'Shamsheer'
p = Person()
print(getattr(p,'name'))
print(getattr(p,'age',20))

# 49. setattr()
class Box: pass
b = Box()
setattr(b,'color','red')
setattr(b,'size',10)
print(b.color, b.size)

# 50. delattr() : Delete an attribute from object. Used to clean up dynamic attributes
class T: x = 5
obj = T()
print(hasattr(obj,'x'))
delattr(T,'x')
print(hasattr(obj,'x'))


# 51. lambda
square = lambda x:x*x
print(square(5))

# 52. reduce()
from functools import reduce
print(reduce(lambda a,b:a+b, [1,2,3]))

# 53. open()
with open("test.txt","w") as f:
    f.write("Hello test file")
with open("test.txt","r") as f:
    print(f.read())

# 54. iter()
lst = [10, 20, 30]
it = iter(lst)
print(next(it))
print(next(it))

# 55. next()
nums = iter([1,2,3])
print(next(nums))
print(next(nums))
print(next(nums, 'done'))


# 56. globals()
x = 100
g = globals()
print('x' in g)
print(g['x'])


# 57. locals()
def show():
    a=10
    print(locals())
show()

# 58. exec()
exec("print(5*2)")

code = 'x = 5\nprint(x * 2)'
exec(code)

# 59. eval()
result = eval('3 + 4 * 2')
print(result)
print(eval('[x**2 for x in range(4)]'))

print(eval("3+4*2"))

# 60. compile()
code = compile("print(2+2)","<str>","exec")
exec(code)

# 61. len (again)
d = {'a':1,'b':2,'c':3}
s = {1,2,3,4}
print(len(d))
print(len(s))


# 62. memoryview()
data = bytearray(b'hello')
mv = memoryview(data)
print(mv[0])
print(bytes(mv[1:3]))

# 63. bytearray()
ba = bytearray(b'hello')
ba[0]=72
print(ba)

# 64. frozenset()
fs = frozenset([1,2,3,2,1])
print(fs)
d = {fs: 'value'}
print(d[fs])

# 65. slice()
lst = [0,1,2,3,4,5,6,7,8,9]
s = slice(2,8,2)
print(lst[s])
print('abcdefgh'[s])


# 66. object()
o = object()
print(type(o))
print(isinstance(o, object))

# 67. super()
class A:
    def speak(self): return "sound"
class B(A):
    def speak(self): return super().speak()+" woof"
print(B().speak())

# 68. property()
class Circle:
    def __init__(self,r): self.r=r
    @property
    def area(self):
        import math
        return round(math.pi*self.r*self.r,2)
print(Circle(5).area)

# 69. staticmethod()
class Math:
    @staticmethod
    def add(a,b): return a+b
print(Math.add(3,4))

# 70. classmethod()
class D:
    def __init__(self,x): self.x=x
    @classmethod
    def create(cls,x):
        return cls(x)
print(D.create(5).x)

# 71. zip_longest()
from itertools import zip_longest
a=[1,2,3]; b=['a','b']
for x in zip_longest(a,b,fillvalue='-'):
    print(x)


# 72. __import__()
m = __import__('math')
print(m.sqrt(16))

# 73. breakpoint() (skip actual use)
x=10
y=x*2
print(x,y)

# 74. NotImplemented
class MyNum:
    def __init__(self,v):
        self.v=v
    def __eq__(self,other):
        if isinstance(other,MyNum):
            return self.v==other.v
        return NotImplemented
print(MyNum(3) == MyNum(3))
print(MyNum(3) == 5)


# 75. __len__()
class Stack:
    def __init__(self): self.data=[]
    def push(self,v): self.data.append(v)
    def __len__(self): return len(self.data)
s=Stack()
s.push(1); s.push(2)
print(len(s))