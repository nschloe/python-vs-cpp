# Python vs. C++

It is an often reiterated statement that

> Interpreted code is always slower then compiled code. We need speed! That's why we're
> using C/C++ in our project.

This assumption is based on the correct observation that large loops like for a dot
product of two vectors `u`, `v`, are faster in C,
```c++
double out = 0.0
for (int k=0; k < n; k++) {
   out += u[k] * v[k];
}
```
than in Python:
```python
out = 0.0
for k in range(n):
    out[k] += u[k] * v[k]
```
If you care about speed, you wouldn't do either of the above loops, though. In Python,
most everyone does
```python
import numpy

out = numpy.dot(u, v)
```
anyway. For C/C++,
[Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page),
[CBLAS](http://www.netlib.org/blas/#_cblas), and [Boost](https://www.boost.org/) come to
mind.

This repository contains a comparison of some common costly numerical operations between
C++ and Python.

As always, comments and suggestions are welcome!


### Dot product of two vectors

<img src="https://nschloe.github.io/python-vs-cpp/dot-product-vectors.svg" width="100%"> | <img src="https://nschloe.github.io/python-vs-cpp/dot-product-vectors-relative.svg" width="100%">
:--------:|:--------:|

### Matrix-matrix product

<img src="https://nschloe.github.io/python-vs-cpp/matrix-matrix-products.svg" width="100%"> | <img src="https://nschloe.github.io/python-vs-cpp/matrix-matrix-products-relative.svg" width="100%">
:--------:|:--------:|

### Sum entries in a vector

<img src="https://nschloe.github.io/python-vs-cpp/sum.svg" width="100%"> | <img src="https://nschloe.github.io/python-vs-cpp/sum-relative.svg" width="100%">
:--------:|:--------:|

### Add two vectors

<img src="https://nschloe.github.io/python-vs-cpp/sum-vectors.svg" width="100%"> | <img src="https://nschloe.github.io/python-vs-cpp/sum-vectors-relative.svg" width="100%">
:--------:|:--------:|


### License
The code in this respository is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
