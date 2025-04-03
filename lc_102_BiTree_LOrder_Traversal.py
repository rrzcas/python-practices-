#lc_102_BiTree_LOrder_Traversal

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])  # Initialize queue with root node
        result = []
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()  #fifo
                level.append(node.val) #lv = current root
                if node.left:
                    q.append(node.left)  #add to end side
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(2)
tree1.left.right = TreeNode(2)
tree1.right.left = None
tree1.right.right = TreeNode(3)
# tree1.left.left.left = tree1 -> cycled
DFX = Solution()
print('Therefore, the answer is ', DFX.levelOrder(tree1))
