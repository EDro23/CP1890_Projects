from dataclasses import dataclass

@dataclass
class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __repr__(self):
        return f'Node: {self.data}'

test1 = Node(2)
print(test1)

@dataclass
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.nextNode
        nodes.append('None')
        return '->'.join(nodes)

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def insert_at(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.nextNode = self.head
            self.head = new_node
            return
        current_node = self.head
        for i in range(position - 1):
            if current_node is None:
                raise IndexError("Position out of bounds")
            current_node = current_node.nextNode
        new_node.nextNode = current_node.nextNode
        current_node.nextNode = new_node


    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        currentNode = self.head
        while currentNode.nextNode:
            currentNode = currentNode.nextNode

        currentNode.nextNode = new_node

    def delete_tail(self, data):
        currentNode = self.head
        if currentNode is None:
            self.head = currentNode
            return
        else:
            while currentNode.nextNode:
                currentNode.head.nextNode = currentNode.nextNode
                currentNode.head = None






llist = LinkedList()
print(llist)
firstNode = Node('a')
llist.head = firstNode

secondNode = Node('b')
thirdNode = Node('c')

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode

llist.insert_at_head("Harv")
llist.insert_at_tail("Harv")
llist.insert_at("HarvDarv",3)

print(llist)

