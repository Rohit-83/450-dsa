#right view of binary tree
#we use level order traversal for this and traverse every level and print the last element
# iterative approach

import LevelWiseInput

def right_view(root):
    if root == None:
        return

    #create a queue to store the nodes in level wise
    que = []
    que.append(root)

    while len(que)>0:
        size = len(que)

        #now we will run loop for every level
        for i in range(1,size+1):
            node = que[0]
            que.pop(0)

            # if i is the last iteration means right most
            if i == size :
                print(node.data)

            if node.left != None:
                que.append(node.left)

            if node.right != None:
                que.append(node.right)

if __name__ == '__main__':
    root = LevelWiseInput.level_wise_input()
    right_view(root)
