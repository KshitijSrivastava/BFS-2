
#Cousins in binary tree 

#(https://leetcode.com/problems/cousins-in-binary-tree/)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self, parent, node, level):
        self.parent = parent
        self.node = node
        self.level = level
        

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        #store x when found
        x_parent = None
        x_level = None
        x_found = False
        
        #store y when found
        y_parent = None
        y_level = None
        y_found = False
        
        queue = []
        #parent, node, level
        queue.append( Node( None, root, 0) )
        
        while len(queue) != 0:
            popped_val = queue.pop(0)
            #find the values of the popped element
            parent = popped_val.parent
            node = popped_val.node
            level = popped_val.level
            
            #print("node_val =", node.val, "level = ", level)
            
            #if both are found then break
            if x_found and y_found:
                break
                
            #if x is found then save them
            if node.val == x:
                x_level = level
                x_parent = parent
                x_found = True
                
            #if y is found save them
            if node.val == y:
                y_level = level
                y_parent = parent
                y_found = True
            
            #if left exists, enqueue left
            if node.left:
                queue.append( Node( node, node.left, level + 1) )
            
            #if right exixsts enqueue right
            if node.right:
                queue.append( Node( node, node.right, level + 1) )
                
        if x_parent != y_parent and x_level == y_level:
            return True
        return False
                
                
            