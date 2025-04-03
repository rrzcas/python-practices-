 #lcsw_100sametree
#lc passed
class TreeNode :
    def __init__ (self , val = 0, left = None ,right = None) :
        self.val=val
        self.left=left
        self.right=right
class Solution :
    def isSameTree (self , Tree1:TreeNode , Tree2 :TreeNode) -> bool :
      if Tree1 is None and Tree2 is None:
        return True
      if Tree1 is None or Tree2 is None:
            return False
      return (Tree1.val == Tree2.val and
            self.isSameTree(Tree1.left, Tree2.left) and
            self.isSameTree(Tree1.right, Tree2.right))
      #Returns T/F

      #Inputting Tree
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = None
tree2.right = TreeNode(2)

tree3 = TreeNode(1)
tree3.left = TreeNode(2)
tree3.right = TreeNode(3)
 
DFX= Solution()

Ans= DFX.isSameTree(tree1,tree3)
print('so the answer of if tree 1 = tree 3 is ' , Ans)

