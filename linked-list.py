# Lined Lists 

class LinkedList:
    def __init__(self, value):
        new_node = Node(value);
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
            new_node = Node(value)
            if self.length == 0:
                 self.head = new_node
                 self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            self.length += 1

    def pop_first(self):
         if self.length == 0:
              return False
         elif self.length == 1:
              self.head = None
              self.tail = None
         else:
              self.head = self.head.next
         self.length -= 1

    def print_list(self):
         temp_node = self.head
         path = ""
         while temp_node is not None:
              path = path + str(temp_node.value) + " - "
              temp_node = temp_node.next
         print(path)

    def pop(self):
         temp_node = self.head
         while temp_node is not None:
                if temp_node.next.next is None:
                     self.tail = temp_node
                     self.tail.next = None
                     break
                temp_node = temp_node.next

    def insert_node_at_position(self, data, position):
        new_node = Node(data)
        if self.head is None:
             self.head = new_node
        else:
            if (position > self.length - 1):
                   print("Index invalid")
            else:
                index = 0
                temp_node = self.head
                while temp_node is not None:
                    if index == position - 1:
                        new_node.next = temp_node.next
                        temp_node.next = new_node
                        break
                    index += 1
                    temp_node = temp_node.next
    def reverse(self):
         temp_node = self.head
         temp_list = []
         

class Node:
      def __init__(self, value):
            self.value = value
            self.next = None


my_linked_list = LinkedList(4)
my_linked_list.append(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.append(40)
my_linked_list.append(50)
my_linked_list.append(60)
# my_linked_list.pop()
# my_linked_list.print_list();
# my_linked_list.prepend(33)
# my_linked_list.print_list();
# my_linked_list.pop_first()
# my_linked_list.print_list()
print("before")
my_linked_list.print_list();
my_linked_list.insert_node_at_position(100, 5)
my_linked_list.print_list();
print("after")



# Sample Linked List Impl
"""

head = {
    value: 10
    next : {
        value : 20
        next: { ----------------> tail
            value: 30
            next: None
        }
    }
}
"""