from sys import stdout


def function_evaluator(coefficients, x):
    # Degree = size of array - 1
    n = len(coefficients) - 1

    # value is used to add everything together
    value = 0

    for i in range(n + 1):
        # add to the net sum in values as coefficients array is traversed and polynomial is evaluated
        value += coefficients[i] * x ** i

    return value


def polynomial_differentiator(coefficients):
    # Degree = size of array - 1
    n = len(coefficients) - 1

    # List to contain the coefficients of the differentiated polynomial
    coefficients_differentiated = []

    for i in range(1, n + 1):
        # d(a*x^n)/dx = n*a*x^(n-1)
        coefficients_differentiated.append(i * coefficients[i])

    return coefficients_differentiated


def main():
    # Get the degree of polynomial function
    n = int(raw_input("Enter degree of polynomial:\t"))

    # Initialize coefficient list
    coefficients = []

    # Accept coefficients from user
    for i in range(n + 1):
        coefficients.append(float(raw_input("Enter coefficient of x^%d:\t" % i)))

    # Get a starting point suggestion from user
    x = float(raw_input("Enter starting point"))

    # Get number of iterations of N-R method to be performed
    iterations = int(raw_input("Enter no. of iterations to perform:\t"))

    # Performing the number of iterations given by user
    for i in range(iterations):
        # Applying N-R formula:
        # x1 = x0 - f(x0)/f'(x0)
        x1 = x - float(function_evaluator(coefficients, x)) / float(
            function_evaluator(polynomial_differentiator(coefficients), x))

        # Showing the user the new value of x and the error between old and new values for the ith iteration
        print "After iteration %d:\tx%d=%f; e%d=%f" % ((i + 1), (i + 1), x1, (i + 1), (x1 - x))

        # Update x to new value of x
        x = x1


if __name__ == "__main__":
    main()
