

# Sum With Carry
```
sum_without_carry = a ^ b
```

# Carry
note that this doesn't consider the carry being added and carried again
```python
carry = (a&b) << 1
```

# find the difference
find-the-difference by xor

# number of bits and value
- time complexity = O(logn), where n is the value
- `x & (x - 1)` would remove the least significant bit

# power of two/four
- and operator on non-power of two/four
- maximum possible value (check whether exist in hex form, 8 charaters 32 bit)
- `x & (x - 1) == 0` if only one bit is present (because the most significant figure will be affected)

# negative
![picture 4](images/0a149bded6a86c953b2b67066e32f67e6fa149dfa8c5be6a14a20d7c5563244b.png)  
`-x = ~x + 1`

Python has no 32-bits limit, need to use mask 
## convert -ve to bit representation

```python
x = -1

# without conversion
print("{0:b}".format(-1))  # -1

# with conversion
mask = 0xFFFFFFFF
x = x & mask
print("{0:b}".format(-1))  # FFFF FFFF
```




## convert bit representation to -ve
```python
a = 0xFFFFFFFF

~(a ^ mask)  # -1
```

## detect negative
```python
max_int = 0x7FFFFFFF # bitmask of 31 1-bits
x > 0x7FFFFFFF  # this is negative

32 bit 
```


# rightmost 1-bit
- `x & (-x)` is a way to keep the rightmost 1-bit and to set all the other bits to 0

# reverse bit
- (too special)
