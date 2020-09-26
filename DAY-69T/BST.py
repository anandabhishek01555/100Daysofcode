class node:
  def __init__(self,val=None):
    self.val=val
    self.left=None
    self.right=None

class BST:
  def __init__(self):
    self.root=None

  def insert(self,root,ele):
    if root == None:   #Tree is Empty
      n1=node(ele)
      return n1
    elif ele<root.val:
      root.left = self.insert(root.left , ele)
    else:
      root.right = self.insert(root.right , ele)
    return root

  def preorder(self,root):
    if root:
      print(root.val)
      self.preorder(root.left)
      self.preorder(root.right)



tr = BST()
tr.root = tr.insert(tr.root,10)
tr.root=tr.insert(tr.root,15)
tr.root = tr.insert(tr.root,5)
tr.root=tr.insert(tr.root,8)
tr.root = tr.insert(tr.root,12)
tr.root=tr.insert(tr.root,16)
tr.root = tr.insert(tr.root,20)
tr.preorder(tr.root)




