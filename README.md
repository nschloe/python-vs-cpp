# Python vs. C++

It is an often reiterated statement that

> Interpreted code is always slower then compiled code. That's why we're using C in our
> project.

This assumption is based on the observation that large loops like for a dot product of
two vectors `u`, `v`, are _much_ faster in C,
```c++
double out = 0.0
for (int k=0; k < n; k++) {
   out += u[k] * v[k];
}
```
than in Python:
```
out = 0.0
for k in range(n):
    out[k] += u[k] * v[k]
```
If you care about speed, you wouldn't do either of the above loops, though. In Python,
most everyone does
```python
out = numpy.dot(u, v)
```
anyway. In C/C++, it's not as easy.
[Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page),
[CBLAS](http://www.netlib.org/blas/#_cblas), and [Boost](https://www.boost.org/) come to
mind.

I


### Dot product of two vectors

<img src="https://nschloe.github.io/python-vs-cpp/dot-product-vectors.svg" width="100%"> |
<img src="https://nschloe.github.io/python-vs-cpp/dot-product-vectors-relative.svg" width="100%">
:--------:|:--------:|

### Matrix-matrix product

<img src="https://nschloe.github.io/python-vs-cpp/matrix-matrix-products.svg" width="100%"> |
<img src="https://nschloe.github.io/python-vs-cpp/matrix-matrix-products-relative.svg" width="100%">
:--------:|:--------:|

### Sum entries in a vector

<img src="https://nschloe.github.io/python-vs-cpp/sum.svg" width="100%"> |
<img src="https://nschloe.github.io/python-vs-cpp/sum-relative.svg" width="100%">
:--------:|:--------:|

### Add two vectors

<img src="https://nschloe.github.io/python-vs-cpp/sum-vectors.svg" width="100%"> |
<img src="https://nschloe.github.io/python-vs-cpp/sum-vectors-relative.svg" width="100%">
:--------:|:--------:|


### License
The code in this respository is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
