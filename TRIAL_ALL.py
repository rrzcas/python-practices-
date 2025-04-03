
#lv order trll - 102

#newfile

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def IfCnnected (self , root : TreeNode =[TreeNode])-> bool :
        if root is None :
            return False
        self(root) == self(root.left )




tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)


tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)


tree1.left.left.left = tree1.right

DFX = Solution()
print('Therefore, the answer is ', DFX.levelOrder(tree1))




#lcsw_27_remove_elements
#remove val from list num- and return count of duplicates

from typing import List , Tuple 
nums_sd = [9,7,6,7,7,7,9,9,0,8,5,2]
val_sd= 7

class Solution:
    def removeElement(self, nums: List[int],val:int) ->int:
     if nums is None :
        return print('num list is None - Error') 
     #if nums is not None :
     unique_list=[]
     vale_list=[]
      #unique_list.append(nums[0])
     for k in range (len(nums)):
            unique_list.append(nums[k])

            #print(f"k:{k} , nums:{nums}  , unique_list:{unique_list}")
            #add all elements thaty i want to remove in listA, len(A)= how many element found in list
            # appended list (num)- A = ans list 
            if nums[k] == val:
             vale_list.append(nums[k])
             #print(f"k1:{k} , nums:{nums}  , vale_list:{unique_list}")

            if len(unique_list)== 0 :
             print(' len of same num s list is 0')
             unique_list.remove(vale_list)
     for i in vale_list:
              if i in unique_list:
                 unique_list.remove(i)
     nums=unique_list[:]
     k=len(unique_list)
     return (k)
     

DFX = Solution()
print( DFX.removeElement(nums_sd,val_sd))

        



