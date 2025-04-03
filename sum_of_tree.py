#sum of tree
class TreeNode :
    def __init__ (self,val=0,left =None ,right=None) :
        self.val=val
        self.left=left 
        self.right = right
class Solution: 
    def sumOfTree (self ,root: TreeNode ) -> int: 
         print ("Calculating SumTree:" + str(root.val) )
         if root is None :
             return 0
        
         sum=root.val

         if root.right is not None :
             print ("Calculating SumTree right child: " + str(root.right.val) )
             sum+=self.sumOfTree(root.right)
         if root.left is not None :
             print ("Calculating SumTree left child: " + str(root.left.val) )
             sum+=self.sumOfTree(root.left)
         print ("Returning sum: " + str(sum))
         return sum 

tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
solution = Solution()
solution.sumOfTree(tree)



