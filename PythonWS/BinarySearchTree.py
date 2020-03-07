class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def AddInOrderToList(self,root, lst):
        if root is None:
            return lst
        self.AddInOrderToList(root.left,lst)
        lst.Add(root.val)
        self.AddInOrderToList(root.right,lst)
        return lst
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.lst=[]
        self.lst=self.AddInOrderToList(root,self.lst)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.lst.count > 0:
            return True
        else:
            return False

        

    # @return an integer, the next smallest number
    def next(self):
        if self.hasNext() is True:
            return self.lst.pop()
