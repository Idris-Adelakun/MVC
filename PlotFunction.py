import numpy as np
import sympy as sp
import matplotlib.pyplot as plt



def plot_function(equation):
    ''' This function is to be used to create a standardised plotting tool for all practice examples
    '''

    x, y = sp.symbols("x y")
    numerical_functions = sp.lambdify(
        (x,y),
        equation,
        "numpy"
    )
    
    # linspace, create x and y ranges
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)

    X, Y = np.meshgrid(x, y)
    Z = numerical_functions(X, Y)

    # Plotting and stylistic choices
    
    figure = plt.figure()
    ax = figure.add_subplot (111, projection='3d')

    ax.plot_surface (X, Y, Z, cmap='viridis')

    #  labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.title(
        rf'3D surface plot of $f(x,y): {sp.latex(equation)}$'
        )

    plt.show()
  
