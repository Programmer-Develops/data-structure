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

# Example usage of the buildTree function
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

root = buildTree(preorder, inorder)
print("Inorder Traversal:", inorder_traversal(root))
print("Preorder Traversal:", preorder_traversal(root))

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, node, x):
        if not node:
            return TreeNode(x)
        if x < node.val:
            node.left = self._insert(node.left, x)
        elif x > node.val:
            node.right = self._insert(node.right, x)
        return node

    # Search (returns True/False)
    def search(self, x):
        return self._search(self.root, x)

    def _search(self, node, x):
        if not node:
            return False
        if x == node.val:
            return True
        elif x < node.val:
            return self._search(node.left, x)
        else:
            return self._search(node.right, x)

    # Find Minimum
    def find_min(self):
        if not self.root:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.val

    # Find Maximum
    def find_max(self):
        if not self.root:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.val

    # Delete (handles 0, 1, or 2 children)
    def delete(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, node, x):
        if not node:
            return None
        if x < node.val:
            node.left = self._delete(node.left, x)
        elif x > node.val:
            node.right = self._delete(node.right, x)
        else:
            # Node found
            if not node.left:          # 0 or 1 child (right)
                return node.right
            elif not node.right:       # 1 child (left)
                return node.left
            # 2 children: replace with inorder successor
            min_val = self._find_min_node(node.right).val
            node.val = min_val
            node.right = self._delete(node.right, min_val)
        return node

    def _find_min_node(self, node):
        while node.left:
            node = node.left
        return node

    # Inorder Traversal (returns sorted list)
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if not node:
            return []
        return self._inorder(node.left) + [node.val] + self._inorder(node.right)
