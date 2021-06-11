class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def userInput():
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinaryTree(rootdata)
    left = userInput()
    right = userInput()
    root.left = left
    root.right = right
    return root



bt1 = BinaryTree(2)
bt2 = BinaryTree(4)
bt3 = BinaryTree(6)
bt4 = BinaryTree(8)
bt5 = BinaryTree(7)
bt6 = BinaryTree(3)
bt1.left = bt2
bt1.right = bt3
bt2.left = bt4
bt2.right = bt5
bt3.left = bt6

def printBinaryTree(root): #we will print the tree in preorder
    if root == None:
        return
    print(root.data,end=":")
    if root.left != None:
        print("L-",root.left.data,end=",")
    if root.right != None:
        print("R-",root.right.data,end="")
    print()
    #now we call the left and right sub tree to do the same task
    printBinaryTree(root.left)
    printBinaryTree(root.right)

if __name__ == '__main__':
    root = userInput()
    printBinaryTree(root)
