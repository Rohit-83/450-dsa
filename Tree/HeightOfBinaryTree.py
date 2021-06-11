import CreateTree


def height(root):
    if root == None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return 1+max(left,right)

if __name__ == '__main__':
    root = CreateTree.userInput()
    print(height(root))
