from sys import stdout

def function_evaluator(coeff, x):
    n = len(coeff) - 1
    value = 0
    print "f(%f) = " % x
    for i in range(n+1):
        value += coeff[i]*x**i
        # stdout.write("%f*(%f^%d) + " % (coeff[i], x, i))
    # print " 0 = %f" % value
    return value

def polynomial_differentiator(coeff):
    n = len(coeff) - 1
    coeff_diff = []
    for i in range(1, n+1):
        coeff_diff.append(i * coeff[i])
    return coeff_diff

n = int(raw_input("Enter degree of polynomial:\t"))

coeff = []

for i in range(n+1):
    coeff.append(float(raw_input("Enter coefficient of x^%d:\t" % i)))

# print "Coefficients of differentiated polynomial:\t", polynomial_differentiator(coeff)

x = float(raw_input("Enter starting point"))

iter = int(raw_input("Enter no. of iterations to perform:\t"))

for i in range(iter):
    x1 = x -float(function_evaluator(coeff, x))/float(function_evaluator(polynomial_differentiator(coeff), x))
    print "After iteration %d:\tx%d=%f; e%d=%f" % ((i+1), (i+1), x1, (i+1), (x1-x))
    x = x1



