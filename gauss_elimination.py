from sys import stdout


def print_array(a):

    # n is the size of the given array
    n = len(a[0])
    # Loop to traverse using row major arrangement
    for i in range(n):
        # Inner loop to print elements column-wise
        for j in range(n):
            # To print on single line without any new line characters at end
            stdout.write(str(a[i][j]) + "\t")
        # Here we need a new line before starting the next row
        print ""


def row_transformation(a, b):
    
    # Check to see if pivot element is 0 --> if so then return [0] or error
    if a[0] == 0:
        return [0]
    
    # Otherwise, get the multiplying factor
    k = float(b[0])/float(a[0])
    # n is size of a = size of b
    n = len(a)
    
    # Traverse the arrays of equal lengths
    for i in range(n):
        # Subtract k times the pivot row from the row to be eliminated
        b[i] -= a[i]*k
    
    # Row reduction successful. Return the result = b
    return b


def gauss_elimination(a, b, n):
    
    # Outer loop; for eliminating all n rows
    for x in range(n):
        # 'l' corresponds to current row with pivot element at position l[x]
        l = a[x]
        # Inner loop to loop through the rest of the n-1-x rows
        for i in range(x, n-1):

            # Print the pass number
            print "\n\n******************************************\n"
            print "PASS:\t%d" % (x+1+i)
            print "\n\n******************************************\n"

            # m corresponds to rows below the current row, 'l'
            m = a[i + 1]
            
            # Augmenting the rhs value before sending to row_reduction function
            l.append(b[x])
            m.append(b[i+1])
            
            #  If pivot element is 0, ask user to rearrange equations
            if l[x] == 0:
                print "Rearrange equation at %d with some other equation" % i
                return 0
            
            #  Print out current row and row to be eliminated for user to double check
            print "l:\t", l, "\nm:\t", m
            #  Print the parameters for the row_reduction function
            print "l[x:]:\t", l[x:], "\nm[x:]:\t", m[x:]
            #  Call the row_reduction function
            c = row_transformation(l[x:], m[x:])
            
            #  Python is pass by reference so we need to pop the last element which would be
            #  the last appended value, which is the rhs value.
            l.pop()
            m.pop()
            
            #  Printing the row transformation results
            print "After row transformation:\t", c
            
            #  Check that no mistake was made inside the function and that it didn't return [0]
            if len(c) > 1:
                #  Update the required columns only, i.e, the ones from a[i+1][x] till the end.
                #  But note that c, the result of the row_reduction function still holds these
                #  column's values starting from index 0.
                for j in range(x, n):
                    print "a[%d][%d] = c[%d] = %f" % ((i+1), j, j, c[j-x])
                    a[i + 1][j] = c[j - x]
                
                #  Update the rhs value as well, which would be the last element in c
                print "b[%d] = c[-1] = %f" % (i+1, c[-1])
                b[i+1] = c[-1]

            #  Output the result after the current pass
            print "After pass %d:" % (x+i+1)
            print "a:\n"
            #  Custom function to print square matrices in a more readable way
            print_array(a)
            print "b=\n"
            print b


def main():
    #  Get input for dimension of array
    n = int(raw_input("Enter the size of the square matrix"))
    
    #  Initialize all elements to 0
    a = [[0 for x in range(n)] for y in range(n)]

    #  Accept the values of array
    for i in range(n):
        for j in range(n):
            a[i][j] = float(raw_input("Enter element %d, %d" % (i, j)))

    print "You have entered: "
    print_array(a)

    #  Get values for b column vector
    b = []
    for i in range(n):
        b.append(float(raw_input("Enter b%d" % i)))

    #  Call the gauss_elimination function
    gauss_elimination(a, b, n)


if __name__ == "__main__":
    main()

