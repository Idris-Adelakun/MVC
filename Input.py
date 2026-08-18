import sympy as sp
# sympy package is good for calculus


def get_equation():
    x, y = sp.symbols("x y")
    user_input = input("Enter f(x,y):\n")

    try:
        equation = sp.sympify(user_input)
        return equation
    except Exception as error:
        print("Invalid equation: {error}")
        return None
