class Solution:
    def triangularSum(self, nums):
        
		
        def perform(nums):
            ln=len(nums)
            for i in range(ln-1):
                a=nums[i]+nums[i+1]
                nums[i]=a%10
			
            return nums[:-1]
            
		
        while len(nums) !=1:
            nums=perform(nums)
            
        return nums[0]