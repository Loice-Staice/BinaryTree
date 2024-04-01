class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

root = TreeNode('L')
node1 = TreeNode('O')
node2= TreeNode('I')
node3 = TreeNode('C')
node4 = TreeNode('E')
node5 = TreeNode('S')
node6 = TreeNode('T')
node7 = TreeNode('G')

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5
node2.right = node6

node6.left = node7

inOrderTraversal(root)

