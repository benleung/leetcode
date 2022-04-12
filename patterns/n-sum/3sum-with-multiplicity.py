class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = Counter(arr)
        unique_numbers = sorted(count.keys())
        
        ans = 0
        
        a,left,right = 0,0,0
        
        def combs(a,b,c):
            matched_tuple = Counter([a,b,c])
            result = 1
            for key, value in matched_tuple.items():
                result *= comb(count[key], value) if count[key] >= value else 0
            return result
        while a < len(unique_numbers):
            first_value = unique_numbers[a]
            two_sum = target - first_value
            if two_sum < 0:
                break
            left = a
            right = len(unique_numbers) - 1
            while left <= right:
                second_value = unique_numbers[left]
                third_value = unique_numbers[right]
                
                if two_sum == second_value+third_value:
                    ans += combs(first_value,second_value,third_value)
                    ans %= 10**9 + 7
                    left += 1
                    right -= 1
                elif second_value+third_value < two_sum:
                    left += 1
                else:
                    right -= 1
            a += 1
            
        
        return ans
        