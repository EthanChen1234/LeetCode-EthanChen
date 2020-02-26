# ref: https://www.jianshu.com/p/43928fd58afb
# ref: https://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding
# ref: https://blog.csdn.net/lzq20115395/article/details/78906863

import queue

class HuffmanNode:
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
    def children(self):
        return ((self.left, self.right))


def create_tree(frequencies):
    p = queue.PriorityQueue()
    for value in frequencies:    # 1. Create a leaf node for each symbol
        p.put(value)             #    and add it to the priority queue
    while p.qsize() > 1:         # 2. While there is more than one node
        l, r = p.get(), p.get()  # 2a. remove two highest nodes
        node = HuffmanNode(l, r) # 2b. create internal node with children
        p.put((l[0]+r[0], node)) # 2c. add new node to queue
    return p.get()               # 3. tree is complete - return root node



freq = [
    (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
    (12.702, 'e'), (2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
    (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
    (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'),
    (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'),
    (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
    (1.974, 'y'), (0.074, 'z')]

node = create_tree(freq)


def walk_tree(node, prefix="", code={}):
    """
    node 是一个tuple(freq, HuffmanNode|character)
    """
    if isinstance(node[1], HuffmanNode): # node[1]是一个HuffmanNode
        code1 = walk_tree(node[1].left, '0', code.copy()) # 这里如果直接传入code会出错
        code2 = walk_tree(node[1].right, '1', code.copy())
        if len(code1) > 0:
            for k, v in code1.items():
                code[k] = prefix + v
        if len(code2) > 0:
            for k, v in code2.items():
                code[k] = prefix + v
    else:  # node[1]是一个字符
        code[node[1]] = prefix
    return(code)

code = walk_tree(node)
# 输出每个字母的编码
for i in sorted(freq, reverse=True):
    try:
        print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])
    except Exception as e:
        print(e)
        continue


