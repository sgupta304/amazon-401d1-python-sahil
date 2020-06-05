from Modules.day_5.day_5.linked_list.node import Node


# https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html
# https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d
# https://medium.com/basecs/whats-a-linked-list-anyway-part-2-131d96f71996


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, key):
        current = self.head
        while current:
            if current.value == key:
                return True
            current = current.next_node
        return False

    def __str__(self):
        current = self.head
        values = '\"'
        while current:
            values += f'{{ {current.value} }} -> '
            current = current.next_node
        values += 'NULL\"'
        return values
