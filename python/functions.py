# functions are of three types
# 1. built-in functions: These are the functions that are present by default in python. e.g. print() function

# 2. user-defined functions: These are the functions that a user defines das per his need.

def function_name(parameter):
    parameter = parameter * 10 
    print(parameter)
    return parameter + 1

function_name(12) #calling a function, o/p: 120
print(function_name(13)) #to get the value returned by the function , o/p: 130 131

# sum function
 
def sum(a,b):
    return a+b

c= sum(2,5)
print(c) #7

# 3. Modules: It is a collection of related functions, classes or variables in python. for e.g. Math

import math
print(dir(math))
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt','ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp','lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']