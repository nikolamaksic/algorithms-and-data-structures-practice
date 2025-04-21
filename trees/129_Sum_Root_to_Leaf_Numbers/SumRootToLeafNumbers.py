class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        totalSum = 0
        def dfs(currSum, currNode):
            nonlocal totalSum
            currSum = currSum*10 + int(currNode.val)
            if not currNode.left and not currNode.right:
                totalSum+=currSum
                return
            if currNode.left:
                dfs(currSum, currNode.left)

            if currNode.right:
                dfs(currSum, currNode.right)
        dfs(0, root)
        return totalSum