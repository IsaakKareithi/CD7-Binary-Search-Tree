# python program to show segment tree operations like
#constuction, query and update

from math import ceil, log2;

#a utility function to get the middle index from corner indexes.
def getMid(s, e):
    return s + (e - s) // 2;

""" A recursive function to get the sum of values in the given range 
of the array. the following are parameters for this function

st --> pointer to segment tree
si --> index of current node in the segment tree.
    Initially 0 is passed as root is always at index 0 
ss & se --> Starting and ending indeces of the segmented 
    represented by the current node 
qs & qe --> Starting and ending indexes of query range"""

def getSumUtil( st, ss, se, qs, qe, si):

    #If the segment of this node is a part of given range,
    # then return the sum of the segment 
    if (qs <= ss and qe >= se):
        return st[si];

    # If the segment of this node is outside the given range,
    #return 0
    if (se < qs or ss > qe):
        return 0;
    
    # if a part of this segemnt overlaps
    # with the given range
    mid = getMid(ss, se);

    return (getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) +
            getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2));

def updateValueUtil(st, ss, se, i, diff, si):

    #Base case: if the input index lies 
    #outside the range of this segment 
    if (i < ss or i > se):
        return;

    # IF the input index is in range of this node, 
    # then update the value of the node and its children 
    st[si] = st[si] + diff;

    if (se != ss):

        mid = getMid(ss, se);
        updateValueUtil(st, ss, mid, i, 
                        diff, 2* si+ 1);
        updateValueUtil(st, mid + 1, se, i, 
                        diff, 2 * si + 2);

#
def updateValue(arr, st, n, i, new_val):

    #Check for erroneous input index
    if (i < 0 or i > n - 1):

        print("Invalid input", end=' ');
        return;

    # get the difference between 
    # new value and old value 
    diff = new_val - arr[i];

    #update the value in array
    arr[i] = new_val;

    #update the values of nodes in segment tree
    updateValueUtil(st, 0, n-1, i, diff, 0);

def getSum(st, n, qs, qe):

    #Check for erroneous input values
    if (qs < 0 or qe > n-1 or qs > qe):

        print("Invalid input", end=' ');
        return -1;

    return getSumUtil(st, 0, n-1, qs, qe, 0);

#A recursive function constructs segment tree for array[ss...se]
# si is the index of current node in the segemtn tree st
def constructSTUtil(arr, ss, se, st, si):

    # If there is one element in the array,
    # store it in the current node of segrment tree and return
    if (ss == se):
        st[si] = arr[ss];
        return arr[ss];

    # if there are more than one elements, 
    #then recur for left and right subtrees
    # and store the sum of value in this node
    mid = getMid(ss, se);

    st[si] = (constructSTUtil(arr, ss, mid, st, si*2 + 1 ) +
              constructSTUtil(arr, mid+1, se, st, si*2 +2 ));

    return st[si];

""" Function to contruct segment tree from given array.
    This function allocates memory for the segement ttree and calls
    constrct() to filll the allocated emory"""
def constructST(arr, n):

    # height of segment tree
    x = (int)(ceil(log2(n)));

    #Maximum size of sement tree
    max_size = 2 * (int)(2**x) - 1;

    #Allocate memory
    st = [0] * max_size;

    #fill the allocated memory at st 
    constructSTUtil(arr, 0, n-1, 0);

    #Return the constructed segment tree
    return st;

#Driver code
if __name__ == '__main__':
    arr =[1,3,5,7,9,11];
    n = len(arr);

    #Bbbuild segment tree from given array
    st = constructST(arr, n);

    #Print sum of value in array from index 1 to 3
    print("Sum of values ")