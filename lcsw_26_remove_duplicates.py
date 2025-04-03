#lcsw_26_remove_duplicates

#Consider the number of unique elements of nums to be k

from typing import List 
nums_sd = [9,7,6,7,7,7,9,9,0,8,5,2] 
class Solution: 
    def removeDuplicates(self, nums: List[int]) -> int:
     if nums is None :
        return print('num list is None - Error')
     if nums is not None :
        ans_list=[]
        ans_list.append(nums[0])
        for k in range (len(nums)):
           #print(f"k:{k} , nums:{nums}  , ans_list:{ans_list}")

           if nums[k] not in ans_list :
              ans_list.append(nums[k]) 
        nums[:] = ans_list 
        return (len(ans_list))

DFX = Solution()
print('Therefore, the answer is ', DFX.removeDuplicates(nums_sd))
print(nums_sd) #num_sd has been over write after fx 

