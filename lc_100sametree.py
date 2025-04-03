#lc_100sametree

#RECURSIVE SOL v
# Definition for a binary tree node.
# Excluded Edge case / Error handling
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode)-> bool:
        if p is None and q is None :
            return True
        if p is None or q is None :
            return False
        if p.val != q.val :
            return False 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

#Tree Inputing
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = None
tree2.right = TreeNode(2)

tree3 = TreeNode(1)
tree3.left = TreeNode(2)
tree3.right = TreeNode(3)

solution = Solution()
      
result = solution.isSameTree(tree1, tree2)
print(result)  

print('4understaingings prints:')
print
