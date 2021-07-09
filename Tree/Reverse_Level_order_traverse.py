#given a binary tree print from bottom
#first approach
#we check height and after geeting height we print nodes for every height
import LevelWiseInput

def height(root):
    if root == None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return 1+max(left,right)

#now we make a function which print nodes at given height
#k = height
def print_nodes_at_height(root,k,d=1):
    if root == None:
        return
    if k==d:
        print(root.data,end=" ")

    print_nodes_at_height(root.left,k,d+1)
    print_nodes_at_height(root.right,k,d+1)

#now we use to traverse from bottom to top by giving height
def reverse_traverse(root,k):
    if root == None:
        return
    while k!=0:
        print_nodes_at_height(root,k)
        k-=1

# one more method is by using queue
def reverse_traverse_levelWise(root):
    if root == None:
        return
    que = []
    ans = []
    que.append(root)
    while len(que)>0:
        node = que.pop(0)
        ans.append(node.data)
        if node.right != None:
            que.append(node.right)
        if node.left != None:
            que.append(node.left)
    return ans[::-1]

if __name__ == '__main__':
    root = LevelWiseInput.level_wise_input()
    k = height(root)
    reverse_traverse(root,k)
    print(reverse_traverse_levelWise(root))