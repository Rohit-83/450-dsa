import CreateTree

def preorderRecursion(root):
    if root == None:
        return
    print(root.data,end=" ")
    preorderRecursion(root.left)
    preorderRecursion(root.right)

def preorderIterative(root):
    if root == None:
        return
    # now we have to use stack bcz in recursion stack is used by system
    # so we try to solve using stack using iterative
    l = []
    l.append(root)
    while  len(l) > 0:
        node = l.pop()
        print(node.data,end=" ")
        if node.right != None:
            l.append(node.right)
        if node.left != None:
            l.append(node.left)


if __name__ == '__main__':
    root = CreateTree.userInput()
    print("recursive approach")
    preorderRecursion(root)
    print()
    print("iterative approach")
    preorderIterative(root)