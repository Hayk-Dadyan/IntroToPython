def calculate_cube(x):
    return x**3

def calculate_square(x):
    return x**2

import pretty_print

def main():
    result1 = calculate_square(2)
    pretty_print.simple_print(result1)
    result2 = calculate_cube(4)
    pretty_print.pro_print(result2)

if __name__ == '__main__':
    main()