#lc_104_MaxDepth_Of_BinaryTree

class TreeNode :
    def __init__ (self ,val = 0 , left = None , right = None ):
        self.val=val
        self.left=left
        self.right=right
        
from typing import Optional 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
     if root is None :
        return 0
    # return int(root.val)
     else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1   



#Inputting Tree
tree1 = TreeNode(2)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)


DFX=Solution()
print('therefore, answer is ', DFX.maxDepth(tree1))


