#Represent polynomials using linked lists.

class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None


# Polynomial Linked List
class Polynomial:
    def __init__(self):
        self.head = None

    # Add a term
    def add_term(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Display polynomial
    def display(self):
        temp = self.head

        while temp:
            print(f"{temp.coefficient}x^{temp.exponent}", end="")

            if temp.next:
                print(" + ", end="")

            temp = temp.next

        print()


# Create polynomial
p = Polynomial()

p.add_term(5, 3)
p.add_term(4, 2)
p.add_term(2, 1)
p.add_term(7, 0)

print("Polynomial:")
p.display()