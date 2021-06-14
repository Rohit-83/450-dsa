import CreateTree

def postOrderRecursive(root):
    if root == None:
        return
    postOrderRecursive(root.left)
    postOrderRecursive(root.right)
    print(root.data,end=" ")

def postOrderIterative(root):
    if root == None:
        return
    #we solve this by using two stack
    stack1 = []
    stack2 = []
    stack1.append(root)
    while len(stack1)>0:
        node = stack1.pop()
        stack2.append(node)
        if node.left != None:
            stack1.append(node.left)
        if node.right != None:
            stack1.append(node.right)
    for i in range(len(stack2)):
        print(stack2.pop().data,end=" ")

if __name__ == '__main__':
    root = CreateTree.userInput()
    postOrderIterative(root)
    print()
    postOrderRecursive(root)