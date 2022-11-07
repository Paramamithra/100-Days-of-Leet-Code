class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n,a in enumerate(nums): #n for first number and a for index of the first number loop for each number
            for m,b in enumerate(nums[n+1:]): #m for second number and b for index of second number (loop through number to the right of first number)
                if target==a+b: #check if sum of two numbers is equal to target
                    return [n,n+m+1] #if yes return index of both the numbers
