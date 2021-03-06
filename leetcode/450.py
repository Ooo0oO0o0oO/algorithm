
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #思路很简单：就是找到待删除节点，然后从删除节点的左子树上找到最大的或者从删除节点的右子树上找到最小的节点为替补节点，最大最小的肯定都是树的末尾，将待删除节点的值转化为替补节点的值，
    # 然后删除替补节点，删除替补节点很简单，因为替补节点一定是叶子节点。直接移除即可。
    def helper(self,root,key):

        def delete(node,val):
            if not node:
                return None

            if node.val > val:
                node.left = delete(node.left,val)
            elif node.val < val:
                node.right = delete(node.right,val)
            else:

                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:

                    maxNode = findLeftMax(node.left) #从node.left中找到最大的值 替代当前node
                    node.val = maxNode.val
                    #从node.left中搜索出maxNode.val删除
                    node.left = delete(root.left,maxNode.val)

            return node




        #找到最大的节点。
        def findLeftMax(node):

            while node.right:
                node = node.right
            return node

        return delete(root,key)

s = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root =  s.helper(root,3)
print(root)