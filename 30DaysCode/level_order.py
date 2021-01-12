import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        value_to_search = []
        value_to_search.append(root)
        while len(value_to_search) > 0:
            value = value_to_search.pop(0)
            if value.left:
                value_to_search.append(value.left)
            if value.right:
                value_to_search.append(value.right)
            print(str(value.data), end=" ")

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
