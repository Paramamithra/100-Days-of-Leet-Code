class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique={} #Create an empty dictionary for saving unique numbers as array functions are slower
        for num in nums: #loop through each number in array
            if num in unique: #if number is already present in previous items of loop
                return True
            else:
                unique[num]=True #Add the number to dictionary
        False
