#lc_101symmetrictree

class TreeNode :
    def __init__ (self , val = 0, left = None ,right = None) :
        self.val=val
        self.left=left
        self.right=right

#Optional = accept both none / valid input
from typing import Optional


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      if root is None :
          return True
      
      
      def isMirror ( TreeLeftC,TreeRightC ) :

        if TreeLeftC is None and TreeRightC is None:
                return True
        if TreeLeftC is None or TreeRightC is None:
                return False
        return ( TreeLeftC.val == TreeRightC.val 
               and isMirror (TreeLeftC.left,TreeRightC.right)
               and isMirror(TreeLeftC.right,TreeRightC.left))
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

Ans= DFX.isSymmetric(tree1)
print('so the answer of if tree 1 = tree 3 is ' , Ans)

