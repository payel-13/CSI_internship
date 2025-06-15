class Node:
    """Represents a node in the singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Manages the singly linked list operations."""
    def __init__(self):
        self.head = None

    def add_node_end(self, data):
        """Add a node with the given data at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Added {data} to the end of the list.")

    def print_list(self):
        """Print all elements in the list."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node in the list (1-based index)."""
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index should be a positive integer.")

        if n == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            print(f"Deleted node at position 1 with data {deleted_data}.")
            return

        current = self.head
        count = 1
        while current and count < n - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            raise IndexError("Index out of range.")

        deleted_data = current.next.data
        current.next = current.next.next
        print(f"Deleted node at position {n} with data {deleted_data}.")


# --- Test the implementation ---
if __name__ == "__main__":
    # Create a LinkedList instance
    ll = LinkedList()

    # Add sample data
    ll.add_node_end(10)
    ll.add_node_end(20)
    ll.add_node_end(30)
    ll.add_node_end(40)

    # Print the list
    ll.print_list()

    # Delete the 2nd node
    try:
        ll.delete_nth_node(2)
    except Exception as e:
        print("Error:", e)

    # Print the list again
    ll.print_list()

    # Try to delete a node from an invalid index
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print("Error:", e)

    # Try to delete from an empty list
    try:
        empty_list = LinkedList()
        empty_list.delete_nth_node(1)
    except Exception as e:
        print("Error:", e)