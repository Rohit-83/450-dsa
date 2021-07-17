# left view of a binary tree
# we would traverse the tree by level order order traversal and print the first of element of
# every level

import LevelWiseInput

def left_view(root):
    if root == None:
        return
    #creating a queue
    que = []
    que.append(root)

    while len(que)>0:
        size = len(que)
        #we will run a loop for every level
        for i in range(1,size+1):
            node = que[0]
            que.pop(0)
            if i == 1:
                print(node.data)

            #and store left and right child of the node in queue
            if node.left != None:
                que.append(node.left)

            if node.right != None:
                que.append(node.right)


if __name__ == '__main__':
    root = LevelWiseInput.level_wise_input()
    left_view(root)