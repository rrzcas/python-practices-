#lcsw_101symmetrictree
#lc passed
class TreeNode :
    def __init__ (self ,val = 0 , left = None , right = None ):
        self.val=val
        self.left=left
        self.right=right
        
from typing import Optional

class Solution :
    def isSymmetric (self , root : Optional [TreeNode ]) -> bool :
     if root is None :
        return True 
     
 
     def isMirror (Tree1stRightC, Tree1stLeftC ) :
              if Tree1stRightC is None and Tree1stLeftC is None :
                  return True
              if Tree1stRightC is None or Tree1stLeftC is None :
                  return False 
               
              
              return (Tree1stRightC.val == Tree1stLeftC.val 
                      and isMirror(Tree1stRightC.right , Tree1stLeftC.left )
                      and isMirror(Tree1stRightC.left , Tree1stLeftC.right)  )
     return isMirror(root.left,root.right)
    

#Inputting Tree
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree1.left.left = TreeNode(2)
tree1.left.right = TreeNode(2)

tree1.right.left = TreeNode(3)
tree1.right.right = TreeNode(3)

DFX= Solution()
Ans = DFX.isSymmetric(tree1)

print ('therefore ', Ans)




              

        