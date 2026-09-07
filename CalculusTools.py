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


def classify_point(equation, critical_points):

    fxx, fyy, fxy = second_derivative(equation)
    classification = []

    for point in critical_points: 

        A = fxx.subs(point)
        B = fxy.subs(point)
        C = fyy.subs(point)
        D = A*C - B**2


        if D>0 and A > 0:
            classification.append("Minimum")

        elif D>0 and A < 0:
            classification.append("Maximum")

        elif D<0:
            classification.append("Saddle Point")
        else:
            classification.append("Inconclusive")

    return classification



# Lesson 2: Chain Rule and Total Differentials

def chain_rule(equation, xeq, yeq, zeq):
    t, x, y, z = sp.symbols("t x y z")
    # later can make take on any variable, for now hardcoded

    xeq = sp.sympify(xeq)
    yeq = sp.sympify(yeq)
    zeq = sp.sympify(zeq)

    w_x = sp.diff(equation, x)
    w_y = sp.diff(equation, y)
    w_z = sp.diff(equation, z)

    dx = sp.diff(xeq, t)
    dy = sp.diff(yeq, t)
    dz = sp.diff(zeq, t)

    # return f"w_x: {w_x}\nw_y: {w_y}\nw_z: {w_z}\ndx: {dx}\ndy: {dy}\ndz: {dz}\n" [DEBUG] 

    sub_map = {
        x: xeq,
        y: yeq,
        z: zeq,
    }
    partials = [w_x, w_y, w_z]
    derivs = [dx, dy, dz]
    eq_sub = [partial.subs(sub_map) for partial in partials] 

    sub_array    = sp.Matrix(eq_sub)
    derivs_array = sp.Matrix(derivs)

    computation = sub_array.dot(derivs_array)


    return computation, f"dw/dt = {computation}"


def total_differential(equation, eval_values): # values will currently need to be stored as list or tuple in order x,y,z (not dynamic)

    x, y, z = sp.symbols("x y z")

    w_x = sp.diff(equation, x)
    w_y = sp.diff(equation, y)
    w_z = sp.diff(equation, z)

    dx = sp.diff(equation, x)
    dy = sp.diff(equation, y)
    dz = sp.diff(equation, z)

    value_map = {
        x:eval_values[0],
        y:eval_values[1],
        z:eval_values[2]
    }

    partials = [w_x, w_y, w_z]

    eq_sub = [partial.subs(value_map) for partial in partials]

    total_differential = eq_sub[0]*dx + eq_sub[1]*dy + eq_sub[2]*dz

    return total_differential


def analyse_level_curve(equation, point):
    '''
    Maps gradient/tangent relationship for level curves
    '''
    x, y,= sp.symbols("x y")

    points = [p.strip() for p in point.split(',')]
    x_point = sp.sympify(points[0])
    y_point = sp.sympify(points[1])

    print(f"x point:{x_point}\ny point:{y_point}")

    equation = sp.sympify(equation)

    contour_level = equation.subs({
        x:x_point, 
        y:y_point
        })

    fx, fy = first_derivative(equation)

    gradient = sp.Matrix([fx, fy])
    gradient_at_point = gradient.subs(
        {
            x:x_point,
            y:y_point
        }
    )

    tangent_vector = (-gradient_at_point[1],gradient_at_point[0])

    return contour_level, gradient_at_point, tangent_vector



    





        



    


