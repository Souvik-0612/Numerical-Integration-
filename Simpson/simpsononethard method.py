import numpy as np

def Simpson(xi, xf, n, f):
	x = np.linspace(xi, xf, n)
	h = (xf - xi)/(n - 1)
	y = f(x)
	
	sum1 = 0
	for i in range(1, n-1, 2):
	   sum1 += y[i]
	
	sum2 = 0
	for i in range(2, n-1, 2):
	   sum2 += y[i]
	
	#Simpson rule    
	sum = h*(y[0] + 4*sum1 + 2*sum2 + y[n-1])/3
    
	return sum
	
#Defination of function	
def f(x):
	return x*x*x
	
	
xi = 1
xf = 2
n = 3
	
print(" ",Simpson(xi, xf, n, f))
