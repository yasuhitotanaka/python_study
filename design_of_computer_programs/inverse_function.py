def inverse(f, delta=1/1024):
    def f_1(y):
        lo, hi = find_bounds(f, y)
        return binary_search(f, y, lo, hi, delta)
    return f_1

def find_bounds(f, y):
    x = 1
    while f(x) < y:
        x = x * 2
        lo = 0 if (x == 1) else x/2
        return lo, x

def binary_search(f, y, lo, hi, delta):
    while lo <= hi:
        x = (lo + hi) / 2
        if f(x) < y:
            lo = x + delta
        elif f(x) > y:
            hi = x - delta
        else:
            return x
    return hi if (f(hi)-y < y-f(lo)) else lo

def square(x): return x*x
def power10(x): return 10**x

log10 = inverse(power10)
sqrt = inverse(square)
cuberoot = inverse(lambda x: x*x*x)

def test():
    import math
    nums = [2,4,6,8,10,99,100,101,1000,10000,20000,40000,100000000]
    for n in nums:
        test1(n, 'sqrt', sqrt(n),math.sqrt(n))
        test1(n, 'log', log10(n), math.log10(n))
        test1(n, '3-rt', cuberoot(n), n**(1./3.))

def test1(n, name, value, expected):
    diff = abs(value-expected)
    print('%6g: %s = %13.7f (%13.7f actual); %.4f diff; %s' % (
        n, name, value, expected, diff,
        ('ok' if diff < .002 else '****BAD****')))