class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=-2**31 #max negative number as max sum
        curr_sum=0 #initialise current sum
        for num in nums: #loop through the numbers
            if curr_sum>0: #if current sum is positive
                curr_sum+=num #add number to current sum
            else:
                curr_sum=num #if negative start adding from current number
            max_sum=max(max_sum,curr_sum) #maximum of current sum and max sum if any in previous
        return max_sum
