import LevelWiseInput
import CreateTree

def min_value(root,minm = 1000000):
    if root == None:
        return
    minm = min (root.data,minm)
    if root.left != None:
        return min_value(root.left,minm)
    return minm

def max_value(root,maxv = -1):
    if root == None:
        return
    maxv = max(root.data,maxv)
    if root.right != None:
        return max_value(root.right,maxv)
    return maxv

if __name__ == '__main__':
    root = LevelWiseInput.level_wise_input()
    min_value = min_value(root)
    max_value = max_value(root)
    CreateTree.printBinaryTree(root)
    print("min value and max value is ",min_value,max_value)



