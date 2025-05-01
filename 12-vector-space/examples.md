# Examples of R2 and R3 Vectors

## R2 Vector 

```py
v1 = R2Vector(x=2, y=3)
v2 = R2Vector(x=0.5,y=1.25)

# Norm
print(v1.norm())            # output: 3.605551275463989

print(f'v1 = {v1}')         # output: v1 = (2, 3)
print(f'v2 = {v2}')         # output: v2 = (0.5, 1.25)

# Add and Sub
v3 = v1 + v2
print(f'v1 + v2 = {v3}')    # output: v1 + v2 = (2.5, 4.25)
v4 = v1 - v2
print(f'v1 - v2 = {v4}')    # output: v1 - v2 = (1.5, 1.75)

# Scalar product and dot product
v5 = v1 * 3
print(f'v1 * 3 = {v5}')     # output: v1 * 3 = (6, 9)
v6 = v1 * v2  
print(f'v1 * v2 = {v6}')    # output: v1 * v2 = 4.75

# Comparison
print(v1 == R2Vector(x=2, y=3)) # output: True
print(v1 != R2Vector(x=2, y=3)) # output: False

print('>', v1 > v2)         # output: > True
print('<', v1 < v2)         # output: < False
print('>=', v1 >= v2)       # output: >= True
print('<=', v1 <= v2)       # output: <= False
print('<=', v1 <= v1)       # output: <= True
```

## R3 Vector

```py
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5,y=1.25, z= 2)

# Norm
print(v1.norm())            # 3.7416573867739413

print(f'v1 = {v1}')         # v1 = (2, 3, 1)
print(f'v2 = {v2}')         # v2 = (0.5, 1.25, 2)

# Add and Sub
v3 = v1 + v2
print(f'v1 + v2 = {v3}')    # v1 + v2 = (2.5, 4.25, 3)
v4 = v1 - v2
print(f'v1 - v2 = {v4}')    # v1 - v2 = (1.5, 1.75, -1)

# Scalar product and dot product
v5 = v1 * 3
print(f'v1 * 3 = {v5}')     # v1 * 3 = (6, 9, 3)
v6 = v1 * v2  
print(f'v1 * v2 = {v6}')    # v1 * v2 = 6.75

# Comparison
print(v1 == R3Vector(x=2, y=3,z=1))     # True
print(v1 != R3Vector(x=2, y=3,z=1))     # False

print('>', v1 > v2)         # > True
print('<', v1 < v2)         # < False
print('>=', v1 >= v2)       # >= True
print('<=', v1 <= v2)       # <= False
print('<=', v1 <= v1)       # <= True


# Cross product (Vector product)
v7 = v1.cross(v2)
print(f'v1 x v2 = {v7}')    # v1 x v2 = (4.75, -3.5, 1.0)
```