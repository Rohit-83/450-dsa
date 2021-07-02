class BinaryTree1:
    def __init__(self,root):
        self.data = root
        self.left = None
        self.right = None

def level_wise_input():
    root_data = int(input())
    if root_data == -1:
        return None
    qu = []
    root = BinaryTree1(root_data)
    qu.append(root)
    while len(qu)>0:
        root1 = qu.pop(0)
        print("left child of",root1.data)
        root_data = int(input())
        if root_data != -1:
            lchild = BinaryTree1(root_data)
            root1.left = lchild
            qu.append(lchild)
        print("right child of",root1.data)
        root_data = int(input())
        if root_data != -1:
            rchild = BinaryTree1(root_data)
            root1.right = rchild
            qu.append(rchild)

    return root

def level_wise_traverse(root):
    if root == None:
        return
    qu = []
    qu.append(root)
    while len(qu)>0:
        node = qu.pop(0)
        print(node.data,end=" ")
        if node.left != None:
            qu.append(node.left)
        if node.right  != None:
            qu.append(node.right)


if __name__ == '__main__':
    root = level_wise_input()
    level_wise_traverse(root)


