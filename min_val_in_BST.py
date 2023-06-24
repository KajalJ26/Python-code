#User function Template for python3

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

#Function to find the minimum element in the given BST.
def minValue(root):
    ##Your code here
    n =root
    if root==None:
        return -1
    while n.left:
        n=n.left
    return n.data    
