import CalculusTools as CT
import sympy as sp
from PlotFunction import plot_function

EQUATION = "x**2*y**2+z**2" # Set equation here



def main():

    # Second derivative test
    try:
        # equation = input("Enter MV equation f(x,y): \n") Uncomment when getting user input
        equation = sp.sympify(EQUATION)
    except Exception as error:
        print("Invalid equation: ", error)

    print(f"Your function is:\n{equation}")
    # print(type(equation)) [DEBUG]

    fx, fy = CT.first_derivative(equation)
    fxx, fyy, fxy = CT.second_derivative(equation)

    # print("fx =", fx)
    # print("fy =", fy)
    # print("fxx =", fxx)
    # print("fyy =", fyy)
    # print("fxy =", fxy)

    # Finding critical point and classifying it
    critical_points = CT.find_critical_points(fx, fy)
    print("Critical points: ", critical_points)
    print("Classification: ", CT.classify_point(equation, critical_points))

    # plot_function(equation)

    test = CT.chain_rule(equation, xeq='t', yeq='t**2', zeq="3*t")   #Testing  
    t_val = float(input("Enter a value for t to evaluate:\n"))
    t = sp.symbols('t')
    result = test[0].subs(t, t_val)
    print(result)


if __name__ == "__main__":
    main()
