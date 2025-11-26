class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf #True if node is leaf 
        self.keys = [] # List of keys
        self.child = []# List of child nodes

#Tree
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)# Root is initially a leaf node
        self.t = t # Minimum degree

    # Insert Node
    def insert(self, k):
        root = self.root
        #If root is full
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root - temp
            temp.child.insert(0, root) # Old root becomes child of new root
            self.split_child(temp, 0) # Split the old root
            self.insert_non_full(temp, k) # Insert the key into the new root
        else:
            self.insert_non_full(root, k) # insert thekey into the current root
    
    def insert_non_full(self, x, k):
        i = len(x.keys) -1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2*self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    #Split the child
    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf) # New node to store (t-1) keys of y
        x.child.insert(i+1, z) # Insert new node as child 
        x.keys.insert(i, y.keys[t-1]) # Insert middle key of y to z
        z.keys = y.keys[t:(2*t) -1] #Copy last [t-1] keys of y to z
        y.keys = y.keys[0:t-1] # Reduces y's keys

        if not y.leaf:
            z.child = y.child[t:2 * t] # Copy last t children of y to  z
            y.child = y.child[0:t]

    #Print the tree
    def print_tree(self, x, l=0):
        print("Level ", l," ", len(x.keys), end=': ')
        for i in x.keys:
            print(i, end=' ')
            print()
            l += 1
            if len(x.child) > 0:
                for i in x.xhild:
                    self.print_tree(i, l)
    
    #Search keys in the tree
    def search_key(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x,i)
            elif x.leaf:
                return None
            else:
                return self.search_key(k, x.child[i])
        else:
            return self.search_key(k, self.root)
        
# main function to run the B-Tree operations 
def main():
    B = BTree(3) # Create a B-tree with minimum degree of 3 
    for i in range(10): #Insert keys into the B-tree
        B.insert((i, 2*i))

    B.print_tree(B.root) # Print the tree structure
    if B.search_key(8) is not None:
        print("\nFound")
    else:
        print("\nNot Found")


if __name__ == "__main__":
    main()
