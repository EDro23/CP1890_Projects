from dataclasses import dataclass


@dataclass
class Node:
    """
    A node class to represent a node.
    """

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __repr__(self):
        return f'Node: {self.data}'


@dataclass
class LinkedList:
    """
    A linked list class for creating linked lists.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.nextNode
        nodes.append('None')
        return '->'.join(nodes)

    def insert(self, data):
        """
        Insert a node into the linked list.
        :param data: Data for the new node
        :return: None
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.nextNode is not None:
            current_node = current_node.nextNode
        current_node.nextNode = new_node

    def delete(self, data):
        """
        Delete a node from the linked list.
        :param data: Data of the node to be deleted
        :return: None
        """
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.nextNode
            return
        current_node = self.head
        while current_node.nextNode is not None:
            if current_node.nextNode.data == data:
                current_node.nextNode = current_node.nextNode.nextNode
                return
            current_node = current_node.nextNode

    def __len__(self):
        """
        Calculate the length of the linked list.
        :return: Length of the linked list
        """
        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.nextNode
        return length


# Create a linked list and use the sample input provided to give an output to Arun.
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(3)
linked_list.insert(5)
linked_list.insert(7)

print(linked_list)
print("Length of the linked list:", len(linked_list))
