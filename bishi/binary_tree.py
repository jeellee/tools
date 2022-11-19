#!coding=utf-8
"""
JZ55 二叉树的深度
         1
        / \    
       2  3
      / \  \ 
    4   5   6
       /
      7
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth2(self, pRoot: TreeNode) -> int:
        # write code here
        """dfs遍历(后序遍历-左右根)"""
        if not pRoot:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1

    def TreeDepth(self, pRoot: TreeNode) -> int:
        """bfs遍历"""
        if not pRoot:
            return 0
        queue, res = [pRoot], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            res += 1
        return res


def func1():
    pRoot = TreeNode("1")

    tree2 = TreeNode("2")
    tree3 = TreeNode("3")
    tree4 = TreeNode("4")
    tree5 = TreeNode("5")
    tree6 = TreeNode("6")
    tree7 = TreeNode("7")

    pRoot.left = tree2
    pRoot.right = tree3

    tree2.left = tree4
    tree2.right = tree5

    tree5.left = tree7

    tree3.right = tree6

    s = Solution()
    res = s.TreeDepth2(pRoot)
    print(res)


if __name__ == "__main__":
    func1()
