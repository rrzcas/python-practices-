#lcsw_226_Invert_BinaryTree
from typing import Optional

class TreeNode :
    def __init__ (self,val :int = 0,left :'TreeNode' = None ,right :'TreeNode' = None) :
    # def __init__ (self,val :int = 0, left = None ,right = None) :
        self.val=val
        self.left=left 
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None :
            return None
        root.right, root.left=root.left,root.right #swapping with tuple
       
        
        
        self.invertTree(root.left) #after looping through all .left untill theres no more .left left
        self.invertTree(root.right) 

        return(root)
    
    def printTree(self, reversed_T : Optional[TreeNode]) -> None:

        if reversed_T is None :
            return None
        
        print(reversed_T.val, end=" ")

        self.printTree(reversed_T .left) #after looping through all .left untill theres no more .left left
        self.printTree(reversed_T .right) 

def sum(int1 : int, int2: int):
    return int1 + int2

    #Inputting Tree
tree1 = TreeNode(1, TreeNode(2, TreeNode(2), TreeNode(2)), TreeNode(3, None, TreeNode(9)))


tree1 = TreeNode(1)
tree1 = TreeNode(TreeNode(1))
tree1 = TreeNode(1, TreeNode(2))


tree1 = TreeNode(1, TreeNode(2, 3))
DFX=Solution()
inverted_tree = DFX.invertTree(tree1)
DFX.printTree(inverted_tree)
#print('therefore, answer is ', ans)

sum(5,2)

TreeNode()