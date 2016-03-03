"""
Script to find intersections of two functions.
g1(x) = x*cos(pi*x) and g2(x) = 1-0.6x^2
Developed by Eric Beauchamp
"""

import newton
import numpy as np
import matplotlib.pyplot as plt

def g1vals(x):
    """
    Return the values of g1(x) and g1'(x)
    to solve with Newton's Method
    """
    g1 = x*np.cos(np.pi*x)
    g1p = np.cos(np.pi*x) - (np.pi*x*np.sin(np.pi*x))

    return g1, g1p    
    
def g2vals(x):
    """
    Return the values of g2(x) and g2'(x) to solve with Newton's method.
    """
    g2 = 1. - 0.6*x**2
    g2p = -1.2*x
    
    return g2, g2p  

def gdiffvals(x):
    """
    Differences betwen g1(x) and g2(x)
    """
    return g1vals(x)[0]-g2vals(x)[0], g1vals(x)[1]-g2vals(x)[1]

x0 = [-3., -2., -1., -0.5, 1., 2., 1.6]
xvals = np.zeros(len(x0))
yvals = np.zeros(len(x0))
    
for i in range(0,len(x0)):
    print " "
    x, iters = newton.solve(gdiffvals, x0[i], debug=False)
    xvals[i] = x
    yvals[i] = g1vals(x)[0]
    
    print "With initial guess x0 = %22.15e" %x0[i]
    print "      solve returns x = %22.15e after %s iterations" %(x, iters)
    print "        g1(x) - g2(x) = %22.15e" %gdiffvals(x)[0]

x = np.linspace(-5.,5.,1000)
y1 = g1vals(x)[0]
y2 = g2vals(x)[0]
plt.clf()
plt.plot(x,y1,'r-', x,y2, 'b-', xvals,yvals, 'ko')
plt.show()

plt.title("Intersections between g1(x) and g2(x)")
plt.savefig('intersections.png')
print "Plot saved as intersections.png"
