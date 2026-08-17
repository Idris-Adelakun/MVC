import numpy as np
import matplotlib.pyplot as plt


def plot_function():
    ''' This function is to be used to create a standardised plotting tool for all practice examples
    '''

    equation = input("Enter Function (f(x, y)):  \n")    
    
    # linspace, create x and y ranges
    x = np.linspace(-100, 100, 1000)
    y = np.linspace(-100, 100, 1000)

    # meshgrid
    X, Y = np.meshgrid(x, y)

    try: 
        Z = eval (equation, {"np": np, "x": X, "y": Y})
    except Exception as error:
        print(f"Invalid equation: {error}")

    # Plotting and stylistic choices
    
    figure = plt.figure()
    ax = figure.add_subplot (111, projection='3d')

    ax.plot_surface (X, Y, Z, cmap='viridis')

    #  labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.title(f'3D surface plot of:{equation}')
    plt.show()


