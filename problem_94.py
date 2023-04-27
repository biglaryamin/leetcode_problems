def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    inord = []
    def inorder(curr=root):
        nonlocal inord
        if curr:
            inorder(curr.left)
            inord.append(curr.val)
            inorder(curr.right)
        return
    inorder()
    return inord