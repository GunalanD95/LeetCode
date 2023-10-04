class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class MyHashMap:

    def __init__(self):
        self.dll = Node(-1, -1)

    def search(self, key, value=None):
        temp = self.dll

        while temp:
            if temp.key == key:
                if value is not None:
                    temp.val = value
                return temp
            temp = temp.next
        return None

    def put(self, key: int, value: int) -> None:
        if not self.search(key, value):
            newNode = Node(key, value)
            tempheadnext = self.dll.next

            if tempheadnext:
                tempheadnext.prev = newNode
            newNode.next = tempheadnext
            newNode.prev = self.dll
            self.dll.next = newNode

    def get(self, key: int) -> int:
        res = self.search(key)
        return res.val if res else -1

    def remove(self, key: int) -> None:
        node = self.search(key)
        if node:
            prevnode = node.prev
            nextNode = node.next

            if prevnode:
                prevnode.next = nextNode

            if nextNode:
                nextNode.prev = prevnode