

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class LevelNode:
    def __init__(self, node, level):
        self.node = node
        self.level = level

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        d = {}
        
        queue = []
        queue.append( LevelNode(root, 0) )
        
        while len(queue) != 0:
            ln = queue.pop(0)
            node = ln.node
            level = ln.level
            
            if level not in d:
                d[level] = node.val
            
            if node.right:
                queue.append( LevelNode(node.right, level + 1) )
            
            if node.left:
                queue.append( LevelNode(node.left, level + 1) )
                
        output = []
        i = 0
        while i in d:
            output.append( d[i] )
            i += 1
            
        return output