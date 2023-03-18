class BrowserHistory:
    def __init__(self, homepage: str):
        self.current_node = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current_node.next = new_node
        new_node.prev = self.current_node
        self.current_node = new_node

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current_node.prev is not None:
                self.current_node = self.current_node.prev
        return self.current_node.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current_node.next is not None:
                self.current_node = self.current_node.next
        return self.current_node.val

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
