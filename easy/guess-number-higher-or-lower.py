# 3'

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while True:
            currentGuess =  (left+right) // 2
            result = guess(currentGuess)
            if result == 0:
                return currentGuess
            elif result == -1:
                right = currentGuess - 1
            elif result == 1:
                left = currentGuess + 1
