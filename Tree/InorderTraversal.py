import CreateTree

def InorderRecursive(root):
    if root == None:
        return
    InorderRecursive(root.left)
    print(root.data,end=" ")
    InorderRecursive(root.right)

def InorderIterative(root):
    l = []
    while True:
        if root != None:
            l.append(root)
            root = root.left
        else:
            if len(l) == 0:
                break
            root = l.pop()
            print(root.data,end=" ")
            root = root.right

if __name__ == '__main__':
    root = CreateTree.userInput()
    InorderRecursive(root)
    print()
    InorderIterative(root)
