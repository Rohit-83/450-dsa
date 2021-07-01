#we have to check the given binary tree is balanced or not
# binary tree is only balanced if its left subtree height and right subtree height is less than
# equal to 1
import CreateTree

def height(root):
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return 1+max(lh,rh)

def CheckTreeBalancer(root):
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh-rh >1 or rh-lh>1:
        return False
    leftChild = CheckTreeBalancer(root.left)
    rightChild = CheckTreeBalancer(root.right)
    if leftChild and rightChild:
        return True
    else:
        return False

# the above code time comlexity is O(logN) and for worst case O(N^2)
# we would optimize the code and its comlexity would be O(N)

def optimizeBalancer(root):
    if root == None:
        return 0,True
    #here we would do extra amount of work for finding height for each node
    lh,leftChild = optimizeBalancer(root.left)
    rh,rightchild = optimizeBalancer(root.right)
    h = 1+max(lh,rh)

    if lh-rh>1 or rh-lh>1:
        return h,False
    if leftChild and rightchild:
        return h,True
    else:
        return h,False

if __name__ == '__main__':
    root = CreateTree.userInput()
    print(CheckTreeBalancer(root))
    print(optimizeBalancer(root))



