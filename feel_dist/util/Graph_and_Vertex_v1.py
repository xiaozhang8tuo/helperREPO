import sys
import math
import json


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}  # 出度点集合 我指向谁 {key: Vertex(obj) value: weight }
        self.adjacent1 = {}  # 入度点集合 谁指向我 {key: Vertex(obj) value: weight }

        self.distance = sys.maxsize  # 记录到出发点的距离，初始化为无穷
        self.distance1 = sys.maxsize  # 记录到目标点的距离，初始化为无穷

        # 优先级队列中的是否访问判断
        self.visited = False

        # 从谁可以找到我
        self.previous = None

        # 节点对应的静态属性
        self.indegree = 0
        self.outdegree = 0
        self.lat = 0
        self.long = 0

    def toJson(self):
        """
        将图保存为json格式
        :return:
        """
        id = " \"id\" : " + "\"" + self.id + "\""
        loc = "\"loc\" : " + "\"" + self.long + "_" + self.lat + "\""
        adjacent = "\"adjacent\" : ["
        for v, v_weight in self.adjacent.items():
            adjacent += "{ " + "\"adj_id\" : " + "\"" + str(v.id) + "\"" + "," \
                        + "\"loc\" : " + "\"" + v.long + "_" + v.lat + "\"" + "," \
                        + "\"weight\" : " + str(v_weight) + "} ,"
        adjacent = adjacent.rstrip(",") + ' ]'

        return "{" + id + ", " + loc + ", " + adjacent + " }"

    def addNeighbor(self, neighbor, weight=0):
        '''
        记录相邻点的距离，如果有多个距离，则取最小的那一条
        :param neighbor:  相邻点(obj)
        :param weight:    顶点到相邻点的距离
        :return:
        '''
        if neighbor not in self.adjacent:
            self.adjacent[neighbor] = weight
        else:
            if weight < self.adjacent[neighbor]:
                self.adjacent[neighbor] = weight

    # def addNeighbor1(self, neighbor, weight=0):
    #     self.adjacent1[neighbor] = weight
    #     self.indegree += 1
    # returns a list

    def getConnections(self):  # neighbor keys
        return self.adjacent.keys()

    def getVertexID(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setDistance(self, dist):
        self.distance = dist

    def resetDistance(self):
        self.distance = sys.maxsize

    def getDistance(self):
        return self.distance

    def setDistance1(self, dest_node):
        self.distance1 = self.getDistance_lat_long(dest_node)

    def getDistance1(self):
        return self.distance1

    def setPrevious(self, prev):
        self.previous = prev

    def resetPrevious(self):
        self.previous = None

    def setVisited(self):
        self.visited = True

    def resetVisted(self):
        self.visited = False

    def getDistance_lat_long(self, node):
        lng1, lat1, lng2, lat2 = self.long, self.lat, node.long, node.lat
        # dx = lng1 - lng2
        # dy = lat1 - lat2
        # b = (lat1 + lat2) / 2.0
        # Lx = math.radians(dx) * 6367000.0 * math.cos(math.radians(b))
        # Ly = 6367000.0 * math.radians(dy)
        Lx = float(lng1) - float(lng2)
        Ly = float(lat1) - float(lat2)
        return math.sqrt(Lx * Lx + Ly * Ly)

    def set_long_lat(self, list):

        self.long = list[0]
        self.lat = list[1]

    def get_long_lat(self):
        return [self.long, self.lat]

    # def getInDegree(self):
    #     return self.indegree
    # def setInDegree(self, degree):11
    #     self.indegree = degree

    def __str__(self):
        return str(self.id) + \
               ' loc:(' + str(self.long) + ',' + str(self.lat) + ')' + \
               ' adjacent: ' + str([x.id for x in self.adjacent])

    def __lt__(self, other):
        return self.distance < other.distance and self.id < other.id


class Graph:
    def __init__(self, directed=False):
        self.vertDictionary = {}  # 存放图中的顶点 dict {key: Vertex.id value: Vertex(obj) }
        self.numVertices = 0
        self.directed = directed

    def __iter__(self):
        return iter(self.vertDictionary.values())

    def toJson(self):
        ret_str = "["
        for v_id, v in self.vertDictionary.items():
            ret_str += v.toJson() + " ,"
        ret_str = ret_str.rstrip(",")
        return ret_str + ']'

    def isDirected(self):
        return self.directed

    def vectexCount(self):
        return self.numVertices

    def addVertex(self, n, loc):
        if n not in self.vertDictionary:
            newVertex = Vertex(n)
            self.numVertices = self.numVertices + 1
            self.vertDictionary[n] = newVertex
            newVertex.set_long_lat(loc.split('_'))
            return newVertex
        else:
            return self.vertDictionary[n]

    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None

    def addEdge(self, frm, f_loc, to, t_loc, cost=sys.maxsize):
        if frm not in self.vertDictionary:
            self.addVertex(frm, f_loc)
        if to not in self.vertDictionary:
            self.addVertex(to, t_loc)

        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
        # self.vertDictionary[to].addNeighbor1(self.vertDictionary[frm], cost)
        # if not self.directed:
        # For directed graph do not add this
        # self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)

    def getVertices(self):
        return self.vertDictionary.keys()

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous

    def getLocIdMap(self):
        """
        返回：map {key：(顶点的经纬度)，value(vert的id)
             like {(2.0, 4.0): '0', (2.0, 1.0): '1'}
        用途：返回map建立KD树， 用于搜索最近节点
        """
        loc2idmap = {}
        for v in self.vertDictionary.values():
            loc2idmap[float(v.long), float(v.lat)] = v.id
        return loc2idmap

    def getEdges(self):
        edges = []
        for key, currentVert in self.vertDictionary.items():
            for nbr in currentVert.getConnections():
                currentVertID = currentVert.getVertexID()
                nbrID = nbr.getVertexID()
                edges.append((currentVertID, nbrID, currentVert.getWeight(nbr)))  # tuple
        return edges

    def getNeighbors(self, v):
        vertex = self.vertDictionary[v]
        return vertex.getConnections()

    def reset(self):
        '''
        重置图中的顶点的各种属性
        '''
        for Vert in self.vertDictionary.values():
            Vert.resetPrevious()
            Vert.resetDistance()
            Vert.resetVisted()

    def __str__(self):
        """
        :return: 输出图中节点的信息
        """
        ret_str = ''
        for v in self.vertDictionary.values():
            ret_str += str(v) + '\n'
        return ret_str
