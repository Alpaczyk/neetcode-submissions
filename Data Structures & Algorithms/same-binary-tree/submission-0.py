# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qu1 = deque()
        qu2 = deque()
        qu1.append(p)
        qu2.append(q)

        while qu1 and qu2:
            q1, q2 = qu1.popleft(), qu2.popleft()

            if not q1 and not q2:
                continue

            if not q1 or not q2:
                return False
            
            if q1.val != q2.val:
                return False

            qu1.append(q1.left)

            qu1.append(q1.right)

            qu2.append(q2.left)

            qu2.append(q2.right)
        
        return True
        