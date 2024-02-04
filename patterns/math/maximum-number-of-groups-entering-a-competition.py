'''
- misread the question (less vs larger than)
- not familiar to qudratic formula (added in algorithm repository)
- 
'''
class Solution:
  '''
  the question is
  1 + ... + x = len(grades)
  find x

  =>
  (1 + x)x/2 = N   # N = len(grades)
  x**2 + x = 2N
  0 = x**2 + x - 2N

  =>
  x = solution2 by qudratic_formula
  '''
  def maximumGroups(self, grades: List[int]) -> int:
      def qudratic_formula(a, b, c):
          d = (b**2) - (4*a*c)
          sol1 = (-b - sqrt(d))/(2*a)
          sol2 = (-b + sqrt(d))/(2*a)
          return (sol1, sol2)
      return floor(qudratic_formula(1, 1, -2*len(grades))[1])
