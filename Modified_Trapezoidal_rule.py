''' Some functional help from Rohan'''

import numpy as np

def Trapezoidal(xi, xf, n, f):
    x = np.linspace(xi, xf, n)
    h = (xf-xi)/(n-1)
    y = f(x)
    sum1 = 0
    for i in range(1, len(y)-1):
        sum1 += y[i]

    # Trapezoidal formula:
    sum2 = 0.5*h*(y[0]+2*sum1+y[len(y)-1])
    return sum2
    
#Function defination
def f(x):
	return x*x
	
#The abs. error btw present and older integration value:
tolerance = float(input("Enter the tolerace "))
	
n = 2
while abs(Trapezoidal(-1, 1, n, f) - Trapezoidal(-1, 1, n+1, f)) > tolerance:
	n += 1
	print(f"The integral is {Trapezoidal(-1, 1, n, f):.5f} for the number of interval", n-1)