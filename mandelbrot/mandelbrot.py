"""
create and plot mandelbrot set
For each complex number, c=x+j*y in the x-y plane [-2,2]x[-2,2], determine 
whether the iterated map, z(n)=z(n-1)^2 + c diverges (not in the set) or
converges (in the set).
For plotting, if the point c is in the set, color it black. If it diverges 
(defined by mod(z)>=2), record number of iterations it took to reach that point.
"""

import numpy as np
import matplotlib.pyplot as plt

def iter_map(c, max_iter):
    """
    Parameters
    ----------
    c : complex float
        complex number in the complex plane in region [-2,2]x[-2,2]
    max_iter: int
              max number of iterations of the quadratic map before convergence
    Returns
    -------
    iter_num: int
              0 if the iterated map has gone for max_iter iterations
              else the number of iterations before mod(z) >= 2
    """
    break_point = 2.0  #if the modulus of c or z is greater than this, it diverges, return -1 (?)
    z = 0+0j   #initial value of z to iterate over for any value of c
    iter_num=0
    while np.abs(z) < break_point and iter_num <= max_iter:
        z = z**2 + c
        iter_num+=1
    if iter_num > max_iter:
        return 0
    else:
        return iter_num
    
    
def histogram_coloring(iter_grid):
    """Input: numpy array of iteration number for each cell or "pixel"
    Perform calculations to plot the mandelbrot set using histogram coloring method
    Find the array, of length max_iter, containing the number of pixels with that number
    of iterations as its iter value, num_iter_per_pixel
    Finally, return an array of same size as iter_grid, containing normalized values from
    num_iter_per_pixel (see the wikipedia article)
    """

max_iter=500

x_min,x_max = -2,1 # borders of grid to evaluate the iter_map over
y_min,y_max = -1,1
num_points = 500 # number of grid points between x_min,x_max (and y_min,y_max)
x = np.linspace(x_min,x_max,num_points) # points on x and y axis to make grid
y = np.linspace(y_min,y_max,num_points)        
xx,yy = np.meshgrid(x,y,sparse=True) # grid in x-y plane

grid=np.empty([num_points,num_points],dtype=int) 
for i in range(num_points):
    for j in range(num_points):
        z_grid=complex(xx[0,i],yy[j,0]) #create complex number from x-y grid
        num_iter = iter_map(z_grid, max_iter)
        grid[i,j] = num_iter

fig,ax = plt.subplots()
ax.pcolormesh(grid,cmap='magma')


