#python program to demonstrate 
#insert opertation in binary search tree

#a utility class that reresents 
#an individual node in Bst

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#A utility function to insert a new node with the given key 
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right =insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root

#A utility function to do inorder tree traversal

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)


# Driver program to test the above 

if __name__ == "__main__":

    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    #print inorder traversal of BST
    inorder(r)