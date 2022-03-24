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
        for j in range(n // 2):  # dun forget
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
```

### Rotate
clockwise 90degree
![picture 2](images/5505dd095820c4ba16128205ad1f1010e42cb9be093ad286cb768664825c4f9d.png)  
- draw the above graph (when i increase for fixed j, how position would vary) -> one arrow
- draw the above graph (when j increase for fixed i, how position would vary) -> another arrow
`matrix[i][j]` -> `matrix[N-j-1][i]`

# diagonal
n-queens
- Positive diagonal: ↗️ r+c
  - 0...N
  - center: (N//2)*2
- Negative diagonal: ↘️ r-c
  - -(N-1)...(N-1)
  - center: 0
![picture 1](images/de88ec5a0c58a3fa978b697b67347bd6fe64b0ee3f6e9b79459fad88ff1ae4a9.png)  
