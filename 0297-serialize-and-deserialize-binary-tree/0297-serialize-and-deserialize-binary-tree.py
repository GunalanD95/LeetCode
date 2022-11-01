from collections import deque
import sys 
sys.setrecursionlimit(10**6)

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "#"
        q = deque()
        q.append(root)
        ans = []

        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()

                if cur_node:
                    ans.append(str(cur_node.val))
                    q.append(cur_node.left)
                    q.append(cur_node.right)
                else:
                    ans.append("#")



        return ",".join(ans)         

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def createNode(strVal):
            if strVal == "#": return None
            return TreeNode(int(strVal))
        
        if data == "#": return None
        A = data.split(",")
        
        root = createNode(A[0])

        q = deque()
        q.append(root)
        
        indx = 1
        while q and indx < len(A):
            cur_node = q.popleft()

            left_node = None 
            if A[indx] != '#':
                left_node = createNode(A[indx])
                q.append(left_node)

            indx += 1
            right_node = None
            if A[indx] != '#':
                right_node = createNode(A[indx])
                q.append(right_node)

            indx += 1

            cur_node.left = left_node
            cur_node.right = right_node 
        return root         

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))