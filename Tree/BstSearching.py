import CreateTree
import LevelWiseInput

def search(root,k):
    if root == None:
        return False
    if root.data == k:
        return True
    if root.data > k:
        return search(root.left,k)
    else:
        return search(root.right,k)

#its time complexity is O(logn) it work like the binary search algorithm

if __name__ == '__main__':
    root = LevelWiseInput.level_wise_input()
    k = 1
    print("result is",search(root,k))
    CreateTree.printBinaryTree(root)