class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x) #Convert in to String
        z=-1 #Initialize a variable to count from end
        for y in range(int(len(x)/2)): #loop from start to middle
            if x[y]==x[z]: #check if mirror values are equal
                z-- #to check next value
            else:
                return False #if not equal return false
        else:
            return True #if all are equal return true
