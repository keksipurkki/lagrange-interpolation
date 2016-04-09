# Lagrange interpolation polynomials

## The math

Read about Lagrange interpolation polynomials at [Wolfram
MathWorld](http://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html)

## The code

The interpolation formula can reformulated in matrix notation:

[The Lagrange interpolation formula](lip_equation.png?raw=true "The Lagrange interpolation formula")

<!--
```tex
Represent any function $f=f(x)$ along \(x=(x_{1}, x_{2},\dots
x_{j},\dots x_{N})\) with a $M-1$ order Lagrange interpolation
polynomial:

\begin{align*}
  f(x_{j}) &\approx \sum_{i=0}^{M} f_i \prod_{k=0}^{M} (\vec{v}^{k}\otimes\vec{u}^{k})_{ij} \\
    &= \sum_{i} f_i \prod_k (\vec{v}\otimes\vec{u})_{ij}^{k}\\
    v^{k}_{j} &= x_{j} - x_{k} \\
    u^{k}_{i} &= \begin{cases}
      (x_{i}-x_{k})^{-1} & i \neq k \\
      1 & i = k
    \end{cases}
\end{align*}

where the grid points $x_{i}$ satisfy $f(x_{i})\equiv f_{i}$ and the
product is over the grid points.
```
-->

