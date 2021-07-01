import CreateTree

def height(root):
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return 1+max(lh,rh)

def diameter(root):
    #basic way we have three ways
    # either we select node and add lh and rh
    # or we find left diameter ar we go for right diameter
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    # now if node is not in the diameter
    leftdiameter = diameter(root.left)
    rightdiameter = diameter(root.right)
    return max(1+lh+rh,leftdiameter,rightdiameter)

# the above code time complexity if O(logN) and for worst case O(N^2)
# so we have to optimize our solution
def optimize_diameter(root):
    #here we would return both height and diameter at same time that prevent our code working time
    if root == None:
        return 0,0
    lh,leftdiameter = optimize_diameter(root.left)
    rh,rightdiameter = optimize_diameter(root.right)
    h = 1+max(lh,rh)
    return h,max(lh+rh+1,leftdiameter,rightdiameter)

if __name__ == '__main__':
    root  = CreateTree.userInput()
    print(diameter(root))
    print(optimize_diameter(root))


