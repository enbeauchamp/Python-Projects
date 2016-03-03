"""
Module for Newton's method
Developed by Eric Beauchamp
"""

def solve(fvals, x0, debug=False):
    """
    Solving Newton's method by iterations of x[k+1] = x[k] - f(x[k])/f'(x[k])
    Up to a tolerance of 10^-14
    Max iterations of 20
    """
    
    maxiter=20
    tol=1.e-14
    x=x0

    if (debug):
        print "Initial guess: x = %22.15e" % x0
    
    for i in range(0,maxiter):
        
        f=fvals(x)[0]
        fp=fvals(x)[1]
        
        # Finished if within desired tolerance
        if abs(f) < tol:
            break
        
        deltaf = f/fp
        x = x-deltaf # Updates the new x.
        
        if (debug):
            print "After %s iterations, x = %22.15e" % (i+1, x)    
        
    return x, i

def fvals_sqrt(x):
    """
    Return f(x) and f'(x) for applying Newton to find a square root.
    """
    f = x**2 - 4.
    fp = 2.*x
    return f, fp

def test1(debug_solve=False):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    from numpy import sqrt
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x
        
if __name__=="__main__":

    print "Running test..."
    test1()
