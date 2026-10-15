#Perform polynomial addition and subtraction by merging lists.
 
class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None


# Polynomial Linked List
class Polynomial:
    def __init__(self):
        self.head = None

    # Add a term in descending order of exponent
    def add_term(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)

        if self.head is None:
            self.head = new_node
            return

        # Insert at beginning
        if exponent > self.head.exponent:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        while temp.next and temp.next.exponent > exponent:
            temp = temp.next

        # If exponent already exists, combine coefficients
        if temp.exponent == exponent:
            temp.coefficient += coefficient
        elif temp.next and temp.next.exponent == exponent:
            temp.next.coefficient += coefficient
        else:
            new_node.next = temp.next
            temp.next = new_node

    # Display polynomial
    def display(self):
        temp = self.head

        while temp:
            if temp.coefficient != 0:
                print(f"{temp.coefficient}x^{temp.exponent}", end="")
                if temp.next and temp.next.coefficient > 0:
                    print(" + ", end="")
                elif temp.next and temp.next.coefficient < 0:
                    print(" ", end="")

            temp = temp.next

        print()


# Add two polynomials
def add_polynomials(p1, p2):
    result = Polynomial()

    a = p1.head
    b = p2.head

    while a and b:
        if a.exponent == b.exponent:
            result.add_term(a.coefficient + b.coefficient, a.exponent)
            a = a.next
            b = b.next

        elif a.exponent > b.exponent:
            result.add_term(a.coefficient, a.exponent)
            a = a.next

        else:
            result.add_term(b.coefficient, b.exponent)
            b = b.next

    # Remaining terms
    while a:
        result.add_term(a.coefficient, a.exponent)
        a = a.next

    while b:
        result.add_term(b.coefficient, b.exponent)
        b = b.next

    return result


# Subtract two polynomials
def subtract_polynomials(p1, p2):
    result = Polynomial()

    a = p1.head
    b = p2.head

    while a and b:
        if a.exponent == b.exponent:
            result.add_term(a.coefficient - b.coefficient, a.exponent)
            a = a.next
            b = b.next

        elif a.exponent > b.exponent:
            result.add_term(a.coefficient, a.exponent)
            a = a.next

        else:
            result.add_term(-b.coefficient, b.exponent)
            b = b.next

    # Remaining terms from P1
    while a:
        result.add_term(a.coefficient, a.exponent)
        a = a.next

    # Remaining terms from P2 with negative sign
    while b:
        result.add_term(-b.coefficient, b.exponent)
        b = b.next

    return result


# Create first polynomial
p1 = Polynomial()
p1.add_term(5, 3)
p1.add_term(4, 2)
p1.add_term(2, 1)
p1.add_term(7, 0)

# Create second polynomial
p2 = Polynomial()
p2.add_term(3, 3)
p2.add_term(2, 2)
p2.add_term(6, 1)
p2.add_term(1, 0)


print("Polynomial 1:")
p1.display()

print("Polynomial 2:")
p2.display()

# Addition
addition = add_polynomials(p1, p2)

print("\nAddition:")
addition.display()

# Subtraction
subtraction = subtract_polynomials(p1, p2)

print("Subtraction:")
subtraction.display()