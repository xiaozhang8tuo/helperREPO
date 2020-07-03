from util.Graph_and_Vertex import Graph
from util.Graph_and_Vertex import Vertex
import util.reader as reader
import heapq


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

    # Put tuple pair into the priority queue
    # Put all vertex into the priority queue
    unvisitedQueue = [(v.getDistance(), v) for v in G]
    heapq.heapify(unvisitedQueue)

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
            newDist = current.getDistance() + current.getWeight(next) + next.getDistance_lat_long(destination)

            if newDist < next.getDistance():
                next.setDistance(newDist)
                next.setPrevious(current)
                print('Updated : current = %s next = %s newDist = %s' \
                      % (current.getVertexID(), next.getVertexID(), next.getDistance()))
            else:
                print('Not updated : current = %s next = %s newDist = %s' \
                      % (current.getVertexID(), next.getVertexID(), next.getDistance()))

        # Rebuild heap  因为节点的属性更新了 而队列中的属性没有更新 重新更新下队列
        # 1. Pop every item
        while len(unvisitedQueue):
            heapq.heappop(unvisitedQueue)
        # 2. Put all vertices not visited into the queue
        unvisitedQueue = [(v.getDistance(), v) for v in G if not v.visited]
        heapq.heapify(unvisitedQueue)

if __name__ == '__main__':
    G = reader.read_data_piece("../data/dijkstra_test.csv")
    source = G.getVertex('6')
    destination = G.getVertex('0')
    for i in source.getConnections():
        print(i.id)
    dijkstra(G, source, destination)



    for v in G.vertDictionary.values():
        print(source.getVertexID(), " to ", v.getVertexID(), "-->", v.getDistance())

    path = [destination.getVertexID()]
    shortest(destination, path)
    print('The shortest path  is: %s' % (path[::-1]))