'''`
 Binary Search Tree (BST) Operations
Goal: Build an ordered structure that supports efficient search and sorted traversal.
1. Implement a BST class with:
• insert(key)
• search(key) (return True/False or node)
• delete(key) (must handle: no child, one child, two children)
• inorder traversal() (prints keys in sorted order)
2. Testing (Required):
Insert a series of numbers, then delete a few to show all cases.
Required Test Plan (Minimum):
• Insert: [50, 30, 70, 20, 40, 60, 80]
• Search: 20, 90
• Delete a leaf node: delete 20
• Delete a node with one child: (you may create one using extra insertions, e.g., insert
65 then delete 60)
• Delete a node with two children: delete 30 or 50
• Print inorder traversal after each deletion.
Short Explanation to Include in report.pdf:
• Why inorder traversal prints a BST in sorted order.
• Time complexity discussion in simple terms (average O(log n), worst O(n) if skewed).
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, key): # This is a helper function for insert, it takes a node and a key to insert
        if key < node.key :
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else: 
                self._insert(node.right, key)

    def insert(self, key): #  This is the main insert function that is called by the user, it checks if the root is None and if so it creates a new node with the key, otherwise it calls the helper function _insert to find the correct position for the new key
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def search(self, key): 
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
        
    def _find_min_node(self, node):
        while node.left:
            node = node.left
        return node
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if not node.left:          # 0 or 1 child (right)
                return node.right
            elif not node.right:       # 0 or 1 child (left)
                return node.left
            min_key = self._find_min_node(node.right).key
            node.key = min_key
            node.right = self._delete(node.right, min_key)
        return node
    
    def inorder(self):
        self._inorder(self.root)
        print()
    
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end = ' ')
            self._inorder(node.right)

print("Testing BST Operations:\n")
print("Inserting: [50, 30, 70, 20, 40, 60, 80]")

bst = BST()

for key in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(key)

print("Searching for 20:", bst.search(20))  # True
print("Searching for 90:", bst.search(90))  # False

print("\nInorder Traversal after insertions:")
bst.inorder()

print("Deleting leaf node (20):")
bst.delete(20)

print("Inorder Traversal after deleting 20:")
bst.inorder()