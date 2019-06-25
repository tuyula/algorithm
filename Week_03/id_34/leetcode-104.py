from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        child = [root.left, root.right]
        max_depth = 0

        for s in child:
            depth = self.maxDepth(root=s)
            max_depth = max(max_depth, depth)

        return max_depth + 1

    def dfs(self, root: TreeNode) -> int:
        if root is None:
            return 0

        stack = deque()
        stack.append((root, 1))
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if not node.left and not node.right:
                max_depth = max(max_depth, depth)

            if node.left and not node.right:
                stack.append((node.left, depth+1))

            if node.right and not node.left:
                stack.append((node.right, depth + 1))

            if node.right and node.left:
                stack.extend([(node.left, depth + 1), (node.right, depth + 1)])

        return max_depth

    def bfs(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = deque()
        queue.append((root, 1))
        max_depth = 0

        while queue:
            node, depth = queue.pop()

            if not node.left and not node.right:
                max_depth = max(depth, max_depth)

            if node.left and not node.right:
                queue.append((node.left, depth + 1))

            if node.right and not node.left:
                queue.append((node.right, depth + 1))

            if node.right and node.left:
                queue.extend([(node.left, depth + 1), (node.right, depth + 1)])

        return max_depth


root = TreeNode(x=3)
node1 = TreeNode(x=9)
node2 = TreeNode(x=20)
node3 = TreeNode(x=15)
node4 = TreeNode(x=7)
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4
s = Solution()
r = s.maxDepth(root)
print(r)
