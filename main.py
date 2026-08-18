from Input import get_equation
from PlotFunction import plot_function
from CalculusTools import second_derivative, classify_point


def main():

    equation = get_equation
    if equation is None:
        return

    print("Your function is:\n{equation}")

    fxx, fyy, fxy = second_derivative(equation)

    plot_function(equation)
    print("fxx =", fxx)
    print("fyy =", fyy)
    print("fxy =", fxy)


if __name__ == "__main__":
    main()
