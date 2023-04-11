def factorial(n):
    if n ==0:
        return 1
    else:
        return n* factorial(n-1)

def ln(x):
    n = 99999999.0
    return n * ((x ** (1/n)) - 1)

def calc_log(base, value):
    if base <= 0 or value <= 0:
        raise ValueError("Logarithms are only defined for positive numbers.")
    elif base == 1:
        raise ValueError("Logarithms with base 1 are not defined.")
    else:
        base = float(base)
        value = float(value)
        ln_value = ln(value)
        ln_base = ln(base)
        return ln_value / ln_base



def sint(t, angle_mode = "rad"):
    if angle_mode == "deg":
        t = t * 180 / 3.14
    value = t
    sign = -1
    n = 150 # precision
    i = 3
    while i < n:
        value = value + ((t ** i) / float(factorial(i)) * sign)
        i = i + 2
        sign = sign * -1
    
    return value

def cost(t, angle_mode = "rad"):
    pi = 3.14159265359
    return sint(float(pi/2) - t, angle_mode)

def tant(t, angle_mode = "rad"):
    ret = sint(t, angle_mode)/cost(t, angle_mode)
    return ret

def sinh(x):
    expression = float(x)
    e = 2.718281828459
    return ((e**expression)-(1/e**expression))/2

def calc_sqrt(X):
    return X ** 0.5

def gamma(x):
    return factorial(x - 1)