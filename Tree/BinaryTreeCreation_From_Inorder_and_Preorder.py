# we have inorder traversal and preorder traversal we have to make binary tree from them
import CreateTree

def tree_Creation(inorder,preorder):
    if len(preorder)==0: #base case
        return None
    root_data = preorder[0]
    root = CreateTree.BinaryTree(root_data)
    indx_root = inorder.index(root_data)
    left_in = inorder[:indx_root]
    right_in = inorder[indx_root+1:]
    len_left_in = len(left_in)
    left_pr = preorder[1:len_left_in+1]
    right_pr = preorder[len_left_in+1:]
    left_ch = tree_Creation(left_in,left_pr)
    right_ch = tree_Creation(right_in,right_pr)
    root.left = left_ch
    root.right = right_ch
    return root

if __name__ == '__main__':
    pre_order = [1, 2, 4, 5, 3, 6, 7]
    in_order = [4, 2, 5, 1, 6, 3, 7]
    root = tree_Creation(in_order,pre_order)
    CreateTree.printBinaryTree(root)

