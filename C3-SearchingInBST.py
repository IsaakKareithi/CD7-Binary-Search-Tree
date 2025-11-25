#Python program to demonstrate insert and search operations in binary search tree

#A utility class that represents a single node in BST

class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

#A utility function to insert a new node with the given key 

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# A utility function to do inorder traversal

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

#A utilityy function to search for a given key
def search(root, key):

    # Base Case: root is null or key is present at root 
    if root is None or root.val == key:
        return root 
    
    #key is greater than root's key
    if root.val < key:
        return search(root.right, key)
    
    #key is smaller than root's key 
    if root.val > key:
        return search(root.left, key)

#Driver program to test the above functions
# Let us create the following BST
#             50
#           /     \
#          30      70
#         /  \    /  \
#        20  40  60  80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inorder traversal of BST
inorder(r)

a = int(input("Enter value to be searched: "))

if search(r, a):
    print(a," is found")
else:
    print(a," is not found")
