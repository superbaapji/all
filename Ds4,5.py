# Construct a dynamic singly linked list with basic operations.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    def insert_after(self, value, data):
        current = self.head
        while current is not None:
            if current.data == value:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        return False
    def delete(self, value):
        if self.head is None:
            return False
        if self.head.data == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        return False
    def search(self, value):
        current = self.head
        position = 0
        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = SinglyLinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
print("Initial list:")
linked_list.display()
linked_list.insert_at_beginning(5)
print("\nAfter inserting 5 at beginning:")
linked_list.display()
linked_list.insert_after(20, 25)
print("\nAfter inserting 25 after 20:")
linked_list.display()
linked_list.delete(20)
print("\nAfter deleting 20:")
linked_list.display()
print("\nSearching for 30:")
print("Position:", linked_list.search(30))


#Example: Music Playlist using a Singly Linked List.
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if self.head is None:
            self.head = new_song
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_song

    def remove_song(self, title):
        if self.head is None:
            print("Playlist is empty.")
            return
        if self.head.title == title:
            self.head = self.head.next
            print(title, "removed.")
            return

        current = self.head

        while current.next is not None:
            if current.next.title == title:
                current.next = current.next.next
                print(title, "removed.")
                return
            current = current.next
        print(title, "not found.")
        
    def show_playlist(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        current = self.head
        number = 1

        while current is not None:
            print(f"{number}. {current.title} - {current.artist}")
            current = current.next
            number += 1

    def search_song(self, title):
        current = self.head
        while current is not None:
            if current.title == title:
                print(f"Found: {current.title} - {current.artist}")
                return
            current = current.next
        print("Song not found.")

playlist = Playlist()

playlist.add_song("Blinding Lights", "The Weeknd")
playlist.add_song("Shape of You", "Ed Sheeran")
playlist.add_song("Believer", "Imagine Dragons")
playlist.add_song("Perfect", "Ed Sheeran")
print("My Playlist:")
playlist.show_playlist()
print("\nSearching for a song:")
playlist.search_song("Believer")
print("\nRemoving a song:")
playlist.remove_song("Shape of You")
print("\nUpdated Playlist:")
playlist.show_playlist()


#Same idea for a To-Do List
class Task:
    def __init__(self, task):
        self.task = task
        self.next = None

class TodoList:
    def __init__(self):
        self.head = None
    def add_task(self, task):
        new_task = Task(task)
        if self.head is None:
            self.head = new_task
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_task
    def complete_task(self, task):
        current = self.head
        previous = None
        while current:
            if current.task == task:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                print("Completed:", task)
                return
            previous = current
            current = current.next
        print("Task not found.")
    def show_tasks(self):
        current = self.head
        while current:
            print("- " + current.task)
            current = current.next

todo = TodoList()
todo.add_task("Study Python")
todo.add_task("Complete assignment")
todo.add_task("Go for a walk")
print("To-Do List:")
todo.show_tasks()
todo.complete_task("Complete assignment")
print("\nUpdated To-Do List:")
todo.show_tasks()


# Create a doubly linked list with forward and backward traversal.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def forward_traversal(self):
        temp = self.head
        print("Forward Traversal:")
        while temp:
            print(temp.data, end=" <-> ")
            last = temp
            temp = temp.next
        print("None")
    def backward_traversal(self):
        temp = self.head
        if temp is None:
            return
        while temp.next:
            temp = temp.next
        print("Backward Traversal:")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)

dll.forward_traversal()
dll.backward_traversal()


#Implement insertion/deletion at head, tail, and specific positions.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def insert_position(self, data, position):
        if position == 1:
            self.insert_head(data)
            return
        new_node = Node(data)
        temp = self.head
        for i in range(1, position - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
    def delete_head(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
    def delete_tail(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        if temp.next is None:
            self.head = None
            return
        while temp.next:
            temp = temp.next
        temp.prev.next = None
    def delete_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position == 1:
            self.delete_head()
            return
        temp = self.head
        for i in range(1, position):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()

dll.insert_head(20)
dll.insert_head(10)
dll.insert_tail(40)
dll.insert_position(30, 3)
print("After Insertion:")
dll.display_forward()
dll.delete_head()
print("After deleting head:")
dll.display_forward()
dll.delete_tail()
print("After deleting tail:")
dll.display_forward()
dll.delete_position(2)
print("After deleting position 2:")
dll.display_forward()


#Use in scenarios like browser history or undo-redo features.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class History:
    def __init__(self):
        self.current = None
    def visit(self, page):
        new_node = Node(page)
        if self.current:
            self.current.next = new_node
            new_node.prev = self.current
        self.current = new_node
    def back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
    def forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
    def show_current(self):
        if self.current:
            print("Current:", self.current.data)

history = History()
history.visit("Google")
history.visit("YouTube")
history.visit("Facebook")
history.show_current()
history.back()
history.show_current()
history.forward()
history.show_current()
