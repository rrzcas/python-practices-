#lc_112_PathSum
targetSum=7.5

class TreeNode :
    def __init__ (self,val=0,left =None ,right=None) :
        self.val=val
        self.left=left 
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, sum):
            if not node.left and not node.right:
                return sum == targetSum
            
            if not node.left and not node.right and sum == targetSum:
                return True
            

            if node.left and dfs(node.left, sum + node.left.val):
                return True
            if node.right and dfs(node.right, sum + node.right.val):
                return True
            return False
        
        return dfs(root, root.val) #REturned (node,sum)
    
#Inputting Tree
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree1.left.left = TreeNode(2)
tree1.left.right = TreeNode(2)

tree1.right.left = None
tree1.right.right = TreeNode(3.5)


DFX=Solution()
print('therefore, answer is ', DFX.hasPathSum(tree1,targetSum))
