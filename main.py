from PlotFunction import plot_function


# 1.Choose the range of \(x\) and \(y\).
# 2.Create a coordinate grid.
# 3.calculate \(z\) for every coordinate.
# 4.Draw those calculated points as a surface.


def main():

    # x = np.linspace(-5, 5, 100)
    # y = np.linspace (-5, 5, 100)
    # X, Y = np.meshgrid(x, y)

    # #Equation of a circle: x^2 + y^2 = r^2, but here we are plotting the surface of the function Z = x^2 + y^2
    # Z = X**2 + Y**2 

    # figure = plt.figure()
    # ax = figure.add_subplot(111, projection='3d') # 111 means 1 row, 1 column, and this is the first subplot

    # # Plotting the surface
    # ax.plot_surface(X, Y, Z, cmap='viridis') #cmap is the color map used for the surface, viridis is a popular color map that goes from dark purple to yellow

    # # add labels
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_zlabel('Z')

    # plt.title('3D Surface Plot of Z = X^2 + Y^2')
    # plt.show() # Display the plot


    # Saddle surface
    plot_function()
    



if __name__ == "__main__":
    main()
