#  图的存储包括邻接矩阵和邻接表 两种方式
class adjacencyArray():
    def __init__(self):
        self.vex = []
        self.edge = []
        self.vexNum = 0
        self.edgeNum = 0

def createAMGraph(withoutDirection=False):
    adjArr = adjacencyArray()
    print("请输入顶点数：")
    adjArr.vexNum = int(input())

    print("请输入边数：")
    adjArr.edgeNum = int(input())

    for i in range(adjArr.vexNum):
        print("请输入顶点信息：")
        adjArr.vex.append(input())
    #初始化边的信息
    for i in range(adjArr.vexNum):
        adjArr.edge.append([])
        for j in range(adjArr.vexNum):
            adjArr.edge[i].append(0)

    print("请顺序输入所有边的首尾节点")
    for index in range(adjArr.edgeNum):
        i = -1
        j = -1
        print("请输入第%d条边的首节点"%index)
        while i == -1:
            v1 = input()
            for i1 in range(len(adjArr.vex)):
                if adjArr.vex[i1] == v1:
                    i=i1
                    break
            if i == -1:
                print("请输入正确的首节顶点")
        print("请输入第%d条边的尾节点" % index)
        while j == -1:
            v1 = input()
            for j1 in range(len(adjArr.vex)):
                if adjArr.vex[j1] == v1:
                    j = j1
                    break
            if j==-1:
                print("请输入正确的尾节点")

        adjArr.edge[i][j] = 1
        if withoutDirection:
            adjArr.edge[j][i] = 1

    return adjArr



if __name__ == "__main__":
    myAdjArr = createAMGraph(withoutDirection=False)

    for i in range(myAdjArr.vexNum):
        for j in range(myAdjArr.vexNum):
            print(myAdjArr.edge[i][j], end="")
        print("\n")

    






