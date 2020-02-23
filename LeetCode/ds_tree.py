class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def create(self, lst):
        root = Node(lst[0])
        length = len(lst)
        if length >= 2:
            root.left = self.create(lst[1])
        if length >= 3:
            root.right = self.create(lst[2])
        return root

    def query(self, root, data):
        if root == None:
            return False
        if root.val == data:
            return True
        elif root.left:
            return self.query(root.left, data)
        elif root.right:
            return self.query(root.right, data)

    def pre_order(self, root):
        if root == None:
            return
        print(root.val, end=' ')
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root):
        if root == None:
            return
        self.in_order(root.left)
        print(root.val, end=' ')
        self.in_order(root.right)

    def post_order(self, root):
        if root == None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val, end=' ')

    def level_order(self, root):
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

if __name__ == '__main__':
    lst = [1, [2, [4], [5]], [3, [6], [7]]]
    binary_tree = BinaryTree()
    tree = binary_tree.create(lst)

    print('in order: ', end=' ')
    binary_tree.in_order(tree)
    print('')
    print('pre order: ', end=' ')
    binary_tree.pre_order(tree)
    print('')
    print('post order: ', end=' ')
    binary_tree.post_order(tree)
    print('')
    print('level order: ', end=' ')
    binary_tree.level_order(tree)


