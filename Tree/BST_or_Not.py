
# we have a binary tree we have to check that it is BST or not
# we would first find max of left subtree and min of right subtree and then compare
import LevelWiseInput

def max_value(root):
    if root == None:
        return -100000  #simalar to -infinite
    left = max_value(root.left)
    right = max_value(root.right)
    return max(left,right,root.data)

def min_value(root):
    if root == None:
        return 100000  #similar to +infinite
    left = min_value(root.left)
    right = min_value(root.right)
    return min(left,right,root.data)

#now we comare these min and max

def checker(root):
    if root == None:
        return True
    left = max_value(root.left)  #find max from left subtree
    right = min_value(root.right) #find min from right subtree
    if root.data < left or root.data > right:
        return False
    #till now we have check for root now we go for subtree
    leftchild = checker(root.left)
    rightchild = checker(root.right)

    return leftchild and rightchild

#the approach we appliede till now has higher time complexity i.e. O(NlogN) or O(N^2)
#so we have to optimize it

def optimize_checker(root):
    if root == None:
        return 1000000,-1000000,True
    leftmin,leftmax,leftchild = optimize_checker(root.left)
    rightmin,rightmax,rightchild = optimize_checker(root.right)
    minm = min(leftmin,rightmin,root.data)
    maxm = max(leftmax,rightmax,root.data)

    if root.data < leftmax or root.data > rightmin:
        return minm,maxm,False
    if leftchild and rightchild:
        return minm,maxm,True
    else:
        return minm,maxm,False


if __name__ == '__main__':
    root = LevelWiseInput.level_wise_input()
    print(checker(root))
    print(optimize_checker(root))