# time complexity without memorization and dp
O(2^n), because Each call to F(n) makes 2 additional calls, to F(n - 1) and F(n - 2). Those 2 calls will then generate 4 calls, which will generate 8, etc
Another way is to think about tree, height is n. total number of leaves are 2^n.
