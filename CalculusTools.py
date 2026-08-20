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


def find_critical_points(A, B):
    '''
    A critical point can be determined when fx=0 and fy=0
    '''
    x, y = sp.symbols("x y")
    return sp.solve([A, B], [x, y]) # solve simultaenously for fx, fy =0, 'solve' must mean=0


def classify_point(A, B, C):
    D = A*C - B**2

    if D>0 and A > 0:
        return "Minimum"

    elif D>0 and A < 0:
        return "Maximum"

    elif D<0:
        return "Saddle point"
    else:
        return "Inconclusive"




