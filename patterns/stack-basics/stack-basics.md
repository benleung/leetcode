# tricks of handling parentheses
example: score-of-parentheses
- keep the number of items in stack same as number of unclosed `(`
  - append when `(`
  - pop when `)`
  - concept of depth is requird
    - (A) has score 2 * A, where A is a balanced parentheses string
    - multiple operation on the same depth ( `stack[-1] += ` )
      - `stack[-1] += node*2 if node!= 0 else 1`
      - `0` as initial value of each depth
- have a dummy head in stack
