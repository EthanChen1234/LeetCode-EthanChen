class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

class SingleLinkedList:
    def __init__(self):
        head_node = Node(0, None)
        self.head = head_node
        self.length = 0

    def is_empty(self):
        if self.head.next:
            return False
        else:
            return True

    def length(self):
        return self.length

    def rear_append(self, elem):
        new_node = Node(elem)
        if self.is_empty():
            self.head.next = new_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node
        self.length += 1

    def head_append(self, elem):
        new_node = Node(elem)
        if self.is_empty():
            self.head.next = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
        self.length += 1

    def traverse(self):
        out = ''
        if not self.is_empty():
            p = self.head.next
            while p.next:
                out += str(p.elem)
                p = p.next
            out += str(p.elem)
        return out

    def find(self, elem):
        if self.is_empty():
            return -1
        else:
            p = self.head.next
            while p:
                if p.elem == elem:
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
            q = self.head
            while q.next != p:
                q = q.next
            q.next = q.next.next
            p.next = None
            self.length -= 1
        else:
            print('del error')

    def clear(self):
        self.head.next = None
        self.length = 0

if __name__ == '__main__':
    linked_list = SingleLinkedList()
    print('is_empty', linked_list.is_empty())

    linked_list.rear_append(3)
    linked_list.rear_append(4)
    linked_list.head_append(5)
    res = linked_list.traverse()
    print('linked list', res)
    print('length', linked_list.length)

    linked_list.modify(4, 8)
    res = linked_list.traverse()
    print('linked list', res)
    print('length', linked_list.length)

    linked_list.del_node(8)
    res = linked_list.traverse()
    print('linked list', res)
    print('length', linked_list.length)

    linked_list.clear()
    res = linked_list.traverse()
    print('linked list', res)
    print('length', linked_list.length)