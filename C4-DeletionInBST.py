# A Binary tree node

class Node:
    #constructot to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# A utility operation to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

# A utility function to insert a new node with given key in BST
def insert(node, key):

    #If tree is empty return a new node
    if node is None:
        return Node(key)
    
    #Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # Return the (unchanged) node pointer
    return node

def minValueNode(node):
    current = Node

    #Loop down to find the leftmost leaf 
    while (current.left is not None):
        current = current.left

    return current 

# Given a BST and a key, the function
# deletes the key and returns the new root 

def deleteNode(root, key):
    
    #Base case 
    if root is None:
        return root 
    
    #If key to be deleted is smaller than the root's key,
    # then it lies in the left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
    
    #if the key to be deletes is greater than the root's key,
    #then it lies in the right subtree
    elif (key > root.key):
        root.right = deleteNode(root.right, key)
    
    #if the key is the same as the root's key,
    #then this is the node to be deleted
    else:

        #node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp 
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        #Node with two children 
        # Get the inordder succesor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        #Copy the inorder succesor 
        root.right = deleteNode(root.right, temp.key)

    return root

# Driver code

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

#
print("Inorder traversal of the subtree is: ")
inorder(root)

print("\nDelete 20 from subtree")
root = deleteNode(root, 20)

print("Inorder traversal of the modified tree: ")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)

print("Inorder traversal of the modified tree: ")
inorder(root)

print("\n Delete 50")
root = deleteNode(root, 50)

print("Inorder traversal of the modified tree: ")
inorder(root)