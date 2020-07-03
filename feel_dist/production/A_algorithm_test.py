from util.Graph_and_Vertex_v1 import Graph
from util.Graph_and_Vertex_v1 import Vertex
import util.reader_v1 as reader
import heapq
import numpy
import json



def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.getVertexID())
        shortest(v.previous, path)
    return


def dijkstra(G, source, destination):
    print('''Dijkstra's shortest path''')
    # Set the distance for the source node to zero
    source.setDistance(0)
    source.setDistance1(destination)

    # Put tuple pair into the priority queue
    # Put all vertex into the priority queue
    # for v in G:
    #     v.setDistance1(destination)

    unvisitedQueue = [(source.getDistance() + source.getDistance1(), source)]
    heapq.heapify(unvisitedQueue)

    for dist, v in unvisitedQueue:
        print([dist, v.id])

    while len(unvisitedQueue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisitedQueue)
        current = uv[1]
        current.setVisited()

        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            newDist = current.getDistance() + current.getWeight(next)

            if newDist < next.getDistance():
                next.setDistance(newDist)
                next.setPrevious(current)
                print('Updated : current = %s next = %s newDist = %s' \
                      % (current.getVertexID(), next.getVertexID(), next.getDistance()))
            else:
                print('Not updated : current = %s next = %s newDist = %s' \
                      % (current.getVertexID(), next.getVertexID(), next.getDistance()))

        # 因为节点的距离属性更新了 而队列中的距离属性没有更新 重新更新下队列
        unvisitedSet = set()   # set： 本次迭代中队列未出队的节点 + 本次迭代中出队节点的adj
        while len(unvisitedQueue):
            uv = heapq.heappop(unvisitedQueue)
            unvisitedSet.add(uv[1])
        unvisitedSet.update({adjV for adjV in current.adjacent if not adjV.visited})

        # #查看下次迭代入队节点的情况
        # print('下轮迭代，入队节点:', end=' ')
        # for i in unvisitedSet:
        #     print(i.id, end=' ')
        # print()

        for v in unvisitedSet:
            v.setDistance1(destination)

        unvisitedQueue = [(v.getDistance() + v.getDistance1(), v) for v in unvisitedSet]
        heapq.heapify(unvisitedQueue)


        for dist, v in unvisitedQueue:
            print([dist, v.id])
        # break

if __name__ == '__main__':
    G = reader.read_data_piece("../data/dijkstra_A.CSV")


    ###################################
    #测试图转json
    #print(G.getVertex('0').toJson())
    #print(G.toJson())
    g_json = G.toJson()
    print(G.getLocIdMap())
    del G
    a = json.loads(g_json)
    #print(type(a))  # list
    G1 = reader.read_json(a)
    ret_map = G1.getLocIdMap()
    #print(a, type(a))

    #json转图

    ###################################

    ####################################

    ####################################




    ###################################
    # dist2idmap = {}
    # for v in G:
    #     print(v.lat, v.long)
    #
    #     dist2idmap[(v.lat, v.long)] = v.id
    # print(dist2idmap)
    ###################################

    ####################################
    # source = G.getVertex('6')
    # destination = G.getVertex('19')
    # print(source)
    # dijkstra(G, source, destination)
    #
    #
    #
    # for v in G.vertDictionary.values():
    #     print(source.getVertexID(), " to ", v.getVertexID(), "-->", v.getDistance())
    #
    # path = [destination.getVertexID()]
    # shortest(destination, path)
    # print('The shortest path  is: %s' % (path[::-1]))