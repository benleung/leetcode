# Basics
### Transpose

```python
def transpose(self, matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
```

### Reflect
```python
def reflect(self, matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
```

### Rotate
clockwise 90degree
`matrix[i][j]` -> `matrix[N-j-1][i]`
- rotate happens -> j and i swap (recite)
- imagine i, j =0,0, after rotating, new position is matrix[N-1][0] -> matrix[N-1-j][i]
 - to double confirm, can imagine i increase for fixed j, should have before/after position would vary
- 
