#lc_111_MinDepth_Of_BinaryTree

class TreeNode :
    def __init__ (self,val=0,left =None ,right=None) :
        self.val=val
        self.left=left 
        self.right = right

class Solution :
    def minDepth(self , root = [TreeNode ])->int :

        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return self.minDepth(root.right) + 1
        elif root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1        
#compare min .( left n right      )
#    
#Inputting Tree
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree1.left.left = TreeNode(2)
tree1.left.right = TreeNode(2)

tree1.right.left = None
tree1.right.right = TreeNode(3)


DFX=Solution()
print('therefore, answer is ', DFX.minDepth(tree1))
