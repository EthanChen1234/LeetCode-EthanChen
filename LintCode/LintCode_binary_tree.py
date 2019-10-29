# coding:utf-8
class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    """二叉树"""
    def __init__(self):
        # 首节点（根节点）
        self.root = None
    def add(self,item):
        """完全二叉树的方式添加"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root] #巧妙
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)


    def breadth_travel(self):
        """广度遍历，层次遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end = ' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def pre_order(self,node):
        """前序遍历"""
        if node is None:
            return
        print(node.elem, end = ' ')
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self,node):
        """中序遍历"""
        if node is None:
            return
        self.in_order(node.lchild)
        print(node.elem, end = ' ')
        self.in_order(node.rchild)

    def post_order(self,node):
        """中序遍历"""
        if node is None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.elem, end=' ')


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.breadth_travel()
    print('')
    tree.in_order(tree.root)
    print('')


