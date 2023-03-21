# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, root):
        result, stack = [], [root]
        while stack:
            node = stack.pop(0)
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                result.append(1001)
        # print(f"  search bfs {result}")
        i = len(result) - 1
        while True:
            # print(f"    result[{i}] == 1001 = {result[i] == 1001}")
            if i == -1:
                # print(f"      case1")
                result = []
                break
            elif result[i] == 1001:
                # print(f"      case2")
                i -= 1
            else: #  result[i] != 1001
                # print(f"      case3")
                result = result[:i+1]
                break
            
        # print(f"  search clear {result}")
        return result
            
        
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        result = True
        tree = self.search(root)
        print(tree)
        for i in range(1, len(tree)):
            if tree[i-1] >= tree[i]:
                result = False
                break
        return result