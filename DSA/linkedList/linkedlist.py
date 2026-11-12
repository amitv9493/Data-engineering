class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def connect(self, node):
        self.next_node = node

    def count_nodes(self, header):
        if header is None:
            return 0
        return 1 + self.count_nodes(header.next)


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

head.connect(node2)
node2.connect(node3)
node3.connect(node4)
node4.connect(node5)
node5.connect(node6)

print("count", Node.count_nodes(head))
