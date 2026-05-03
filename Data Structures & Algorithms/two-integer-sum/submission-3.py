class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for l,i in enumerate(nums):
            seen[i]=l
        print(seen)
        for l,i in enumerate(nums):
            if target-i in seen and l!=seen[target-i]:
                return [l,seen[target-i]]   