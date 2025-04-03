#lcsw_27_remove_elements
#remove val from list num- and return count of duplicates

from typing import List 
nums_sd = [0,1,9,3,7,5,6,3,7,7,7,0,2]
val_sd= 7

class Solution:
    def removeElement(self, nums: List[int],val:int) ->int:
     if nums is None :
        return print('num list is None - Error')
     k=0
     for i in range (len(nums)):
        #for val == nums(i) , k = k +1 , return k 
        if nums[i] != val :
          
           nums[k] = nums[i]
           k+=1
           print(nums[i])
     return (k)
     

DFX = Solution()
print('ans:', DFX.removeElement(nums_sd,val_sd))

        