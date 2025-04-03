#lcsw_01_two_sum


List_sd = [1,3,5,8,9 ]
Target_sd = int(17)

#1
class Solution:
    def twoSum (self,nums,target)->int:
        if nums is None :
         return print('List is None - Error ')
        if nums is not None :
         for i in range (len(nums)): #i = 0,1,2,3,4,etc
           for j in range (len(nums)):
              print(f"i: {i}, j: {j}")
              if i != j and nums[i] + nums[j]== target :
                 return [i,j]
                
         return None
 
DFX = Solution()
print('Therefore, the answer is ', DFX.twoSum(List_sd,Target_sd))

