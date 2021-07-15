#Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of
# all non-leaf nodes interchanged.

import CreateTree

def mirror(root):
    if root == None:
        return
    mirror(root.left)
    mirror(root.right)
    root.left,root.right = root.right,root.left
    return root


if __name__ == '__main__':
    root = CreateTree.userInput()
    CreateTree.printBinaryTree(root)
    root = mirror(root)
    print()
    CreateTree.printBinaryTree(root)