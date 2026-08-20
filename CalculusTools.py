import sympy as sp

def first_derivative(equation):
    x, y = sp.symbols("x y")
    fx = sp.diff(equation, x)
    fy = sp.diff(equation, y)

    return fx, fy


def second_derivative(equation):
    '''
    Takes a SymPy equation and returns:
    fxx, fyy, fxy
    '''
    x, y = sp.symbols ("x y")

    fxx = sp.diff(equation, x, 2)
    fyy = sp.diff(equation, y, 2)
    fxy = sp.diff(equation, x, y)

    return fxx, fyy, fxy


def find_critical_points(fx, fy):
    '''
    A critical point can be determined when fx=0 and fy=0
    '''
    x, y = sp.symbols("x y")
    return sp.solve(
        [fx, fy], [x, y],
        dict=True # solve simultaenously for fx, fy =0, 'solve' must mean=0
    ) 


def classify_point(equation, critical_point):

    fxx, fyy, fxy = second_derivative(equation)

    A = fxx.subs(critical_point)
    B = fxy.subs(critical_point)
    C = fyy.subs(critical_point)

    D = A*C - B**2

    if D>0 and A > 0:
        return "Minimum"

    elif D>0 and A < 0:
        return "Maximum"

    elif D<0:
        return "Saddle point"
    else:
        return "Inconclusive"




