'''
learn
- knowledge about shuffle algorithm (Fisher-Yates Algorithm )
  - swapping n times is ok, no need another array to pop one by one
- python's random.randrange(len(self.nums))
- 
'''


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.after = nums.copy()

    def reset(self) -> List[int]:
        self.after = self.nums.copy()
        return self.after

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            target = random.randrange(len(self.nums))
            self.after[i], self.after[target] = self.after[target], self.after[i]
        return self.after


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
