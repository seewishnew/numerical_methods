from sys import stdout
n = int(raw_input("Enter the size of the square matrix"))

A = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        A[i][j] = float(raw_input("Enter element %d, %d" % (i, j)))

print "You have entered: "
def print_array(A):

    n = len(A[0])
    for i in range(n):
        for j in range(n):
            stdout.write(str(A[i][j]) + "\t")
        print ""
print_array(A)

b = []
for i in range(n):
    b.append(float(raw_input("Enter b%d" % i)))

def row_transformation(a, b):
    if(a[0] == 0):
        return [0]
    k = float(b[0])/float(a[0])
    n = len(a)
    for i in range(n):
        b[i] -= a[i]*k
    return b

def gauss_elimination(A, b):
    for x in range(n):
        l = A[x]
        for i in range(x, n-1):

            print "\n\n******************************************\n"
            print "PASS:\t%d" % (x+1+i)
            print "\n\n******************************************\n"

            m = A[i+1]
            l.append(b[x])
            m.append(b[i+1])
            if l[x] == 0:
                print "Rearrange equation at %d with some other equation" % i
                return 0
            print "l:\t", l, "\nm:\t", m
            print "l[x:]:\t", l[x:], "\nm[x:]:\t", m[x:]
            c = row_transformation(l[x:], m[x:])
            l.pop()
            m.pop()
            print "After row transformation:\t", c
            if(len(c)>1):
                for j in range(n):
                    if(j in range(x+1)):
                        print "A[%d][%d] = 0" % (i+1, j)
                        A[i+1][j] = 0.0
                    else:
                        print "A[%d][%d] = c[%d] = %f" %(i+1, j, j, c[j])
                        A[i+1][j] = c[j]
                print "b[%d] = c[-1] = %f" % (i+1, c[-1])
                b[i+1] = c[-1]

            print "After pass %d:" % (x+i+1)
            print "A:\n"
            print_array(A)
            print "b=\n"
            print b

gauss_elimination(A, b)

