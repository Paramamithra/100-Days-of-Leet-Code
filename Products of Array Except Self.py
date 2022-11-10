#consider nums = [1,2,3,4]
#expected output shall be [24,12,8,6]
#product of left of number will be [1,1,2,6]
#product of right of number will be [24,12,4,1]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct=[1] 
        rightProduct=[1]*len(nums) #fill all with 1 so that reverse scan does not have index error
        answer=[]
        for i in range(1,len(nums)):
            leftProduct.append(leftProduct[i-1]*nums[i-1]) #save product number to the left of number
        for i in range(len(nums)-2,-1,-1):
            rightProduct[i]=rightProduct[i+1]*nums[i+1] #save product number to the right of number
        for i in range(len(nums)):
            answer.append(leftProduct[i]*rightProduct[i]) #multiply each
        return answer
