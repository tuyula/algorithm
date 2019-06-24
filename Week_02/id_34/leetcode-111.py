from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        children = [root.left, root.right]

        if not any(children):
            return 1

        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1

    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left or root.left:
            return self.minDepth2(root.right) + self.minDepth2(root.left) + 1
        return min(self.minDepth2(root.left), self.minDepth2(root.right)) + 1

    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = deque()
        stack.append((root, 1))
        min_depth = float('inf')

        while stack:
            node, depth = stack.pop()

            if not node.left and not node.right:
                min_depth = min(min_depth, depth)

            if node.right and not node.left:
                stack.append((node.right, depth + 1))

            if node.left and not node.right:
                stack.append((node.left, depth + 1))

            if node.left and node.right:
                stack.extend([(node.right, depth+1), (node.left, depth+1)])

        return min_depth

    def bfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append((root, 1))
        min_depth = float('inf')

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                min_depth = min(min_depth, depth)

            if node.left and not node.right:
                queue.append((node.left, depth + 1))

            if node.right and not node.left:
                queue.append((node.right, depth + 1))

            if node.right and node.left:
                queue.extend([(node.right, depth + 1), (node.left, depth + 1)])

        return min_depth


# root = TreeNode(x=3)
# node1 = TreeNode(x=9)
# node2 = TreeNode(x=20)
# node3 = TreeNode(x=15)
# node4 = TreeNode(x=7)
# root.left = node1
# root.right = node2
# node2.left = node3
# node2.right = node4

# root = TreeNode(x=1)
# node1 = TreeNode(x=2)
# root.left = node1
# s = Solution()
# r = s.dfs(root=root)
# print(r)