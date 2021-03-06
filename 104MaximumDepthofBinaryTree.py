# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxleafDepth(self, node, depth):
        if not node.left and not node.right:
            return depth
        elif node.left and not node.right:
            return self.maxleafDepth(node.left, depth+1)
        elif node.right and not node.left:
            return self.maxleafDepth(node.right, depth+1)
        else:
            m_leftdepth = self.maxleafDepth(node.left, depth+1)
            m_rightdepth = self.maxleafDepth(node.right, depth+1)
            return m_leftdepth if m_leftdepth > m_rightdepth else m_rightdepth

    def maxDepth(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            m_depth = 0
            if root is None:
                return m_depth
            return self.maxleafDepth(root, m_depth+1)
