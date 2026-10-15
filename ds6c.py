#Use structured representation to reinforce node manipulation.
class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    def add_term(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)

        # Empty list
        if self.head is None:
            self.head = new_node
            return

        # Insert at beginning
        if exponent > self.head.exponent:
            new_node.next = self.head
            self.head = new_node
            return

        # Find correct position
        temp = self.head

        while temp.next and temp.next.exponent > exponent:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head

        while temp:
            print(f"({temp.coefficient}, {temp.exponent})", end=" → ")
            temp = temp.next

        print("NULL")

p = Polynomial()

p.add_term(5, 3)
p.add_term(4, 2)
p.add_term(2, 1)
p.add_term(7, 0)

p.display()