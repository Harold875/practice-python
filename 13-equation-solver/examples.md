# Examples of Linear Equations and Quadratic Equations

## Linear Equation

```py
lin_eq = LinearEquation(2, 3)
print(solver(lin_eq))
```

Output:

```

----Linear Equation-----

       2x +3 = 0        

-------Solutions--------

       x = -1.500       

--------Details---------

slope =            2.000
y-intercept =      3.000

```

## Quadratic Equation

### Example 1

```py
quadr_eq = QuadraticEquation(1,2,1)
print(solver(quadr_eq))
```

Output:

```

---Quadratic Equation---

    x**2 +2x +1 = 0     

-------Solutions--------

       x = -1.000       

--------Details---------

concavity =      upwards
min =    (-1.000, 0.000)

```

### Example 2

```py
quadr_eq = QuadraticEquation(-11,-1,1)
print(solver(quadr_eq))
```

Output:

```

---Quadratic Equation---

   -11x**2 -x +1 = 0    

-------Solutions--------

      x1 = -0.350       
      x2 = +0.259       

--------Details---------

concavity =    downwards
max =    (-0.045, 1.023)

```