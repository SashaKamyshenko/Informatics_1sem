class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def get(self, index):
        if index >= self.len:
            print("error")
            return
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def append(self, new):
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.len += 1

    def insert(self, index, val):
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.len:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        elif self.len == 0:
            self.head = self.tail = new_node
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
            prev_node = cur.prev

            new_node.prev = prev_node
            new_node.next = cur

            prev_node.next = new_node
            cur.prev = new_node

        self.len += 1

    def len(self):
        return self.len

    def remove(self, val):
        cur = self.head
        if cur is None:
            print("error")
            return

        if cur.val == val:
            self.head = cur.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.len -= 1
            return

        while cur:
            if cur.val == val:
                break
            cur = cur.next

        if cur is None:
            print("error")
            return

        if cur.next:
            cur.next.prev = cur.prev
        else:
            self.tail = cur.prev

        if cur.prev:
            cur.prev.next = cur.next

        self.len -= 1


l = LinkedList()
for i in range(10):
    l.append(i)

print(l.get(6))
l.insert(6, 9)
print(l.get(6))

print(l.len)
l.remove(7)
print(l.len)
