"""
    Dummy project, with dummy code
"""
import sys


def add(first_number , second_number):
    """Adds two numbers"""
    return first_number  + second_number


def multiply(first_number , second_number):
    """Multiplies two numbers"""
    return first_number  * second_number


def main():
    """Main method"""
    print(add(2, 3))
    print(multiply(2, 3))


if __name__ == '__main__':
    sys.exit(main())
