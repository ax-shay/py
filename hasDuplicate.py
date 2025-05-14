class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       nums_dict = {}
       for i in range(len(nums)):
          if nums_dict.get(nums[i]) is not None:
             return True
          nums_dict[nums[i]] = i
       return False
