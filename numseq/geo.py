"""Functions dealing with numbers that can be arranged in geometric shapes"""


def square(n):
    """Square a number

    square(n) takes a number n as the argument
    and returns the square of that number
    """
    return n*n


def triangle(n):
    """Return number of units in a triangle

    triangle(n) takes a number n as the argument (representing the number
    of units that make up the foundation or base of a triangle) and returns the
    total number of units in the triangle
    """
    results = []
    count = 1
    number = n
    results.append(number)
    while n > count:
        results.append(number - 1)
        number -= 1
        count += 1
    return sum(results)


def cube(n):
    """Return a cube number

    cube(n) takes a number n as the argument and returns the cube number
    of n.  Each cube number can be represented by a cube made up of unit
    cubes
    """
    return n**3
