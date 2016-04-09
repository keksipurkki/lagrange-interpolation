#!/usr/bin/env python2
# encoding: utf-8

"""

  An implementation of Lagrange interpolation polynomials for 1D
  functions

"""

from numpy import *

class Lip(object):
    """Interpolate `y` with a `n-1` order LIP."""

    def __init__(self, y, n=7):
        self.f = array([])
        self.y = y
        self.n = n
        self.g = []


    def __call__(self, x, ncell):
        """

        Parameters:
        -----------
        x : ndarray
            Coordinates where `y` will be interpolated.

        ncell: integer
            Split the interval x[0]..x[-1] to `ncell` cells

        """

        f = ones((x.size, self.n))

        # Partition the input variable to cells,
        # raises an error if not divisible evenly.
        cells = split(x, ncell)
        maxs = map(size, cells)
        k = 0
        for j, c in enumerate(cells):

            fcell = ones((maxs[j], self.n, self.n))

            # Grid
            g = linspace(c.min(), c.max(), self.n)
            self.g.append(g)

            v = array([c - l for l in g ])
            u = array([i - g for i in g ]).T
            u = where(u != 0, u, 1.0)

            for i in range(self.n):
                fcell[:,:,i] = v[i][:,None] / u[i] # "Outer division"
                fcell[:,i,i] = self.y(g[i])

            #print k, k + c.size -1
            f[k:k + c.size] = prod(fcell, 2)
            k += c.size

        self.f = f
        return sum(f, 1)

    @property
    def lips(self):
        return (self.f).T

#    # Works only for small ranges
#    def interpolate_raw(self, x):
#        g = linspace(x.min(), x.max(), self.n)
#        v = array([x - l for l in g ])
#        u = array([i - g for i in g ]).T
#        u = where(u != 0, u, 1.0)
#        f = ones((x.size, self.n, self.n))
#
#        for i in range(self.n):
#            f[:,:,i] = v[i][:,None] / u[i] # "Outer division"
#            f[:,i,i] = self.y(g[i])
#
#        f = prod(f, 2)
#        return sum(f, 1)

def main():

  y = lambda x: sin(2*pi*x) * exp(-x)
  y_inter = Lip(y)
  x = linspace(-2, 2, 100)

  print "x\tExact\tInterpolated\tAbs. error/%"
  for xi, yi, yj in zip(x, y(x), y_inter(x, 4)):
    print "{:.3f}\t{:.3f}\t{:.3f}\t\t{:.3f}".format(xi, yi, yj, abs(yi-yj) * 100)


if __name__ == '__main__':
  main()
