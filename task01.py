class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
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
        else:
            cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int, min_index=0):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        for _ in range(min_index-1):
            prev = cur
            cur = cur if not cur.next else cur.next
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        """Функція, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами"""

        # Якщо у списку один елемент, то він є і оберненим списком
        cur_node = self.head
        if cur_node.next == None:
            return cur_node
        
        prev_node = None
        while cur_node.next:  # Перебираємо всі елементи, не включаючи останній
            next_node = cur_node.next
            cur_node.next = prev_node
            
            prev_node = cur_node
            cur_node = next_node
        # Робимо останній елемент першим
        cur_node.next = prev_node
        self.head = cur_node
        return self.head

    def sort_list(self):
        """Алгоритм сортування для однозв'язного списку"""
        # Якщо у списку один елемент, то він є і відсортованим
        cur_node = self.head
        if cur_node.next == None:
            return cur_node

        first_non_sorted = 1 # до якого елементу списку відсортовано
        while cur_node.next:
            insert_node = self.head
            for _ in range(first_non_sorted):
                insert_node = insert_node.next
            # вилучаємо елемент зі списку для вставлення у відповідне місце вже відсортованої частини списку    
            self.delete_node(insert_node.data, min_index=first_non_sorted) 
            
            # Пошук відповідного місця
            if insert_node.data <= self.head.data:
                self.insert_at_beginning(insert_node.data)
                first_non_sorted += 1
            else:
                i = 1
                node_ = self.head
                while i < first_non_sorted and insert_node.data > node_.next.data:
                    i += 1
                    node_ = node_.next
                self.insert_after(node_, insert_node.data)
            insert_node = self.head
            for _ in range(first_non_sorted):
                insert_node = insert_node.next
            if insert_node.next:
                first_non_sorted += 1
            else:
                return self
    
def comb_sort_list(llist: LinkedList, llist_2: LinkedList):
    node_ = llist.head
    while node_.next:
        node_ = node_.next
    node_.next = llist_2.head
    llist.sort_list()
    return llist


def main():
    llist = LinkedList()
    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(1)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(9)
    llist.insert_at_beginning(7)
    llist.insert_at_beginning(15)
    llist.insert_at_beginning(22)

    # Друк зв'язного списку
    print("Однозв'язний список:")
    llist.print_list()

    llist.reverse()

    # Друк зв'язного списку
    print("Реверсування однозв'язного списку:")
    llist.print_list()

    print("Сортування однозв'язного списку:")
    llist.sort_list()
    # Друк зв'язного списку
    llist.print_list()

    llist_2 = LinkedList()
    llist_2.insert_at_beginning(36)
    llist_2.insert_at_beginning(27)
    llist_2.insert_at_beginning(5)
    llist_2.insert_at_beginning(4)
    llist_2.insert_at_beginning(3)

    print("Однозв'язний список_2:")
    llist_2.print_list()

    print("Об'єднання двох списків в один відсортований список:")
    llist_comb = comb_sort_list(llist, llist_2)
    llist_comb.print_list()

if __name__ == '__main__':
    main()