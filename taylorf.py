import sympy as sy

#Taylor series function
def taylor(function, y, n, x = sy.Symbol('x')):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x, i).subs(x, y[0]))/(factorial(i))*(x - y[0])**i
        i += 1
    return p
    #sy.Simbol associate the variable x to letter 'x'
    #diff difference between to consecutive iterations
    #subs replace the previous variable for the next one