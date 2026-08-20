from Input import get_equation
from PlotFunction import plot_function
from CalculusTools import second_derivative



def main():

    equation = get_equation()
    if equation is None:
        return

    print(f"Your function is:\n{equation}")
    print(type(equation))

    fxx, fyy, fxy = second_derivative(equation)

    print("fxx =", fxx)
    print("fyy =", fyy)
    print("fxy =", fxy)

    plot_function(equation)
    


if __name__ == "__main__":
    main()
