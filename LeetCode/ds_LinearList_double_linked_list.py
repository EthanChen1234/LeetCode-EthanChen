class Node:
    def __init__(self, data=None):
        self.elem = data
        self.pre = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.length = 0

    def is_empty(self):
        if self.head.next == self.tail:
            return True
        else:
            return False

    def length(self):
        return self.length

    def traverse(self):
        res = ''
        p = self.head.next
        while p != self.tail:
            res += str(p.elem)
            p = p.next
        return res

    def rear_append(self, val):
        new_node = Node(val)
        # before
        before_node = self.tail.pre
        before_node.next = new_node
        new_node.pre = before_node
        # after
        self.tail.pre = new_node
        new_node.next = self.tail
        #
        self.length += 1

    def head_append(self, val):
        new_node = Node(val)
        # after
        after_node = self.head.next
        after_node.pre = new_node
        new_node.next = after_node
        # before
        new_node.pre = self.head
        self.head.next = new_node
        #
        self.length += 1

    def find(self, val):
        if self.is_empty():
            return -1
        p = self.head.next
        while p:
            if p.elem == val:
                return p
            p = p.next
        return -1

    def modify(self, old, new):
        p = self.find(old)
        if p != -1:
            p.elem = new
        else:
            print('modify error')

    def del_node(self, val):
        p = self.find(val)
        if p != -1:
            before, after = p.pre, p.next
            before.next = after
            after.pre = before
            p.pre, p.next = None, None
            self.length -= 1
        else:
            print('del node error')

    def insert_before(self, val, new):
        p = self.find(val)
        if p != -1:
            new_node = Node(new)
            # before
            before = p.pre
            before.next = new_node
            new_node.pre = before
            # after
            new_node.next = p
            p.pre = new_node
            #
            self.length += 1
        else:
            print('insert error')

    def clear(self):
        self.head.next = self.tail
        self.tail.pre = self.head
        self.length = 0


if __name__ == '__main__':
    linked_list = DoubleLinkedList()
    linked_list.rear_append(1)
    linked_list.rear_append(5)
    out = linked_list.traverse()
    print('linked_list', out)
    print('length', linked_list.length)

    linked_list.head_append(3)
    linked_list.head_append(7)
    out = linked_list.traverse()
    print('linked_list', out)
    print('length', linked_list.length)

    linked_list.del_node(7)
    out = linked_list.traverse()
    print('linked_list', out)
    print('length', linked_list.length)

    linked_list.insert_before(1, 9)
    out = linked_list.traverse()
    print('linked_list', out)
    print('length', linked_list.length)

    linked_list.clear()
    out = linked_list.traverse()
    print('linked_list', out)
    print('length', linked_list.length)



