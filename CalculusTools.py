import sympy as sp


def second_derivative(equation):
    '''
    Takes a SymPy equation and returns:
    fxx, fyy, fxy
    '''
    x, y = sp.symbols ("x y")

    fxy = sp.diff(equation, x, y)
    fxx = sp.diff(equation, x, 2)
    fyy = sp.diff(equation, y, 2)

    return fxy, fxx, fyy


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


def find_stationary_points():
    pass

