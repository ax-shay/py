class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:     
      seen_dict = {}
      for i in range(len(nums)):
         seek = target - nums[i]
         if seen_dict.get(seek) is not None:
            return ([i, seen_dict.get(seek)])
         else:
            seen_dict[nums[i]] = i

if __name__ == '__main__':
   s = Solution()
   print(s.twoSum([2, 4, 5, 6], 7))

