class Graph(object):
    def __init__(self, mat, unconn=0):
        self.matrix_check(mat)

        vnum = len(mat)
        self.mat = [mat[i][:] for i in range(vnum)]
        self.unconn = unconn
        self.vnum = vnum

    def matrix_check(self, matrix):
        row_num = len(matrix)
        for x in matrix:
            if len(x) != row_num:
                raise ValueError('Not Square Matrix')

    def vertex_num(self):
        return self.vnum

    def invalid(self, v):
        return 0 > v or v >= self.vnum

    def add_edge(self, vi, vj, val=1):
        if self.invalid(vi) or self.invalid(vj):
            raise ValueError("error")
        self.mat[vi][vj] = val

    def out_edges(self, vi):
        if self.invalid(vi):
            raise ValueError("error")
        return self._out_edges(self.mat[vi], self.unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:  # 当前行中不等于0的位置
                edges.append((i, row[i]))
        return edges

if __name__ == '__main__':
    mat = [[0, 0, 3],
           [4, 0, 6],
           [0, 8, 9]]
    g = Graph(mat)
    print(g.out_edges(1))