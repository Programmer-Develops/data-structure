class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    root_idx = inorder.index(preorder[0])
    
    inorder_left = inorder[:root_idx]
    inorder_right = inorder[root_idx+1:]
    
    preorder_left = preorder[1:1 + len(inorder_left)]
    preorder_right = preorder[1 + len(inorder_left):]
    
    root.left = buildTree(preorder_left, inorder_left)
    root.right = buildTree(preorder_right, inorder_right)
    
    return root

# Helper functions for verification
def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

def preorder_traversal(root):
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []

# Example usage
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

root = buildTree(preorder, inorder)
print("Inorder Traversal:", inorder_traversal(root))
print("Preorder Traversal:", preorder_traversal(root))