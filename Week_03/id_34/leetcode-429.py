from typing import List
from collections import deque


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return [[]]

        visited, queue = [], deque([root])
        level = 0

        while queue:
            visited.append([])
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                visited[level].append(node.val)
                queue.extend(node.children)
            level += 1

        return visited
