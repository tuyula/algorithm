# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def _recurse_tree(current_node: TreeNode):
            if not current_node:
                return False

            left = _recurse_tree(current_node.left)

            right = _recurse_tree(current_node.right)

            mid = current_node == p or current_node == q

            if mid + left + right >= 2:
                self.ans = current_node

            return mid or left or right

        _recurse_tree(current_node=root)
        return self.ans

    def dfs(self):
        pass

# root = TreeNode(x=3)
# node1 = TreeNode(x=5)
# node2 = TreeNode(x=6)
# node3 = TreeNode(x=2)
# node4 = TreeNode(x=7)
# node5 = TreeNode(x=4)
# node6 = TreeNode(x=1)
# node7 = TreeNode(x=0)
# node8 = TreeNode(x=8)
# root.left = node1
# node1.left = node2
# node1.right = node3
# node3.left = node4
# node3.left = node5
# root.right = node6
# node6.left = node7
# node6.right = node8
# s = Solution()
# r = s.lowestCommonAncestor(root=root, p=node1, q=node5)
# print(r.val)