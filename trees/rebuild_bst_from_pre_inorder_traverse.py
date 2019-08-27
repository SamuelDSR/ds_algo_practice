class BTNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder_traverse(root, func):
    """preorder traverse of binary tree, i.e., itself, then left, then right"""
    func(root.value)
    if root.left is not None:
        preorder_traverse(root.left, func)
    if root.right is not None:
        preorder_traverse(root.right, func)


def inorder_traverse(root, func):
    """inorder traverse of binary tree, i.e., first left, then itself, then right"""
    if root.left is not None:
        inorder_traverse(root.left, func)
    func(root.value)
    if root.right is not None:
        inorder_traverse(root.right, func)


def postorder_traverse(root, func):
    """post order traverse of binary tree, i.e., first left, right, then itself"""
    if root.left is not None:
        inorder_traverse(root.left, func)
    if root.right is not None:
        inorder_traverse(root.right, func)
    func(root.value)


def rebuild_bt(preorder_list, inorder_list):
    assert len(preorder_list) == len(inorder_list), "no equal length"
    if (not preorder_list) or (not inorder_list):
        return None

    root = BTNode(preorder_list[0])

    root_index_in_inorder = inorder_list.index(root.value)
    left_sub_tree_inorder = inorder_list[:root_index_in_inorder]
    right_sub_tree_inorder = inorder_list[root_index_in_inorder+1:]
    #  print("inorder")
    #  print(left_sub_tree_inorder)
    #  print(right_sub_tree_inorder)

    if root_index_in_inorder != 0:
        last_left_index_in_preorder = preorder_list.index(inorder_list[root_index_in_inorder-1])
        left_sub_tree_preorder = preorder_list[1:last_left_index_in_preorder+1]
        right_sub_tree_preorder = preorder_list[last_left_index_in_preorder+1:]
    else:
        left_sub_tree_preorder = []
        right_sub_tree_preorder = preorder_list[1:]

    #  print("preorder")
    #  print(left_sub_tree_preorder)
    #  print(right_sub_tree_preorder)

    root.left = rebuild_bt(left_sub_tree_preorder, left_sub_tree_inorder)
    root.right = rebuild_bt(right_sub_tree_preorder, right_sub_tree_inorder)

    return root


preorder_list = [3, 20, 15, 7]
inorder_list = [3, 15, 20, 7]
root = rebuild_bt(preorder_list, inorder_list)
preorder_traverse(root, print)
print("----")
inorder_traverse(root, print)
