# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        visited, queue = [], deque([root])
        level = 0

        while queue:
            visited.append([])
            length = len(queue)

            for _ in range(length):
                node = queue.popleft()
                child = [node.left, node.right]
                childs = [c for c in child if c]
                visited[level].append(node.val)
                queue.extend(childs)
            level += 1

        ret = []
        for i in range(level-1, -1, -1):
            ret.append([])
            ret[level-1-i].extend(visited[i])

        return ret
