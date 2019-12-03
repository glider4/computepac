# computepac
A Python package of mathematical functions, iterative solvers, numerical analysis, and more.

## bisection
The Bisection method is an iterative numerical analysis scheme to find the roots of an equation.

To find the root of your equation between a certain lower and upper bound, run:

```python
import sympy as sym

f = sym.Function('f')
x = sym.Symbol('x')
f = '''YOUR EQUATION'''

bisection(f, lower bound, upper bound, accuracy desired)
```

The output format includes number of iterations to achieve desired accuracy, the root as calculated,
and the total time the program needed for computation.

```python
[num_itr, root, total_time]
```


## newton_raphson
The Newton-Raphson Method (or just Newton's Method) is an iterative scheme using derivatives to find
the root of a function.  To find the root of your equation, make a guess as to where it is, and run:

```python
import sympy as sym

f = sym.Function('f')
x = sym.Symbol('x')
f = '''YOUR EQUATION'''

newton_raphson(f, guess of root, accuracy desired)
```

The output format includes number of iterations to achieve desired accuracy, the root as calculated,
and the total time the program needed for computation.

```python
[num_itr, root, total_time]
```


 ## How to run tests
This package uses `pytest` for unit testing.

To run tests locally in a terminal, run the following three lines:
```bash
cd your_path/computepac
chmod +x test.sh
./test.sh
```
All unit tests are located in the tests directory.  One sample test was built for debugging purposes
(`test_sample.py`).  This unit test will always pass.  If it does not run, then something is wrong with
pytest or your local setup (make sure you are in the right directory).
