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
	return np.sin(x)
	
#The abs. error btw present and older integration value:
tolerance = float(input("Enter the tolerace "))
	
n = 2
a = 0
b = np.pi

#
while abs(Trapezoidal(a, b, n, f) - Trapezoidal(a, b, n+1, f)) > tolerance:
	
	e = abs(Trapezoidal(a, b, n, f) - Trapezoidal(a, b, n+1, f))
	print(f"{Trapezoidal(a, b, n, f):.5f}\t {e:.3f}\t {n-1}")
	n += 1
