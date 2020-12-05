def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(l):
    def f(a,b):
        return a
    return l(f)

def cdr(l):
    def f(a,b):
        return b
    return l(f)



x=cons(1,cons(2,3))
print(car(cdr(x)))