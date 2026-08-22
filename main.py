import CalculusTools as CT
import sympy as sp
from PlotFunction import plot_function

EQUATION = "12*x**2+y**3-12*x*y" # Set equation here



def main():


    try:
        # equation = input("Enter MV equation f(x,y): \n") Uncomment when getting user input
        equation = sp.sympify(EQUATION)
    except Exception as error:
        print("Invalid equation: ", error)

    print(f"Your function is:\n{equation}")
    # print(type(equation)) [DEBUG]

    fx, fy = CT.first_derivative(equation)
    fxx, fyy, fxy = CT.second_derivative(equation)

    print("fx =", fx)
    print("fy =", fy)
    print("fxx =", fxx)
    print("fyy =", fyy)
    print("fxy =", fxy)

    # Finding critical point and classifying it
    critical_points = CT.find_critical_points(fx, fy)
    print("Critical points: ", critical_points)
    print("Classification: ", CT.classify_point(equation, critical_points))

    plot_function(equation)
    


if __name__ == "__main__":
    main()
