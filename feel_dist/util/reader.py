# code-utf8
from util.Graph_and_Vertex import Graph
from util.Graph_and_Vertex import Vertex


def read_data_piece(file_name):
    '''
        读取linked表，创建对应的节点和街道，并且返回对应的 node_dict 和 street_dict
        Args:
            file_name: linked表
        Return：
            G: 数据块对应的图对象(存储着vertex和 edge的信息）
        '''
    fp = open(file_name)
    line_num = 0
    G = Graph(True)
    for line in fp:
        if line_num == 0:
            line_num += 1
            continue

        [link_id, fnode_id, fnode_longitude, fnode_latitude, tnode_id, tnode_longitude, tnode_latitude, link_len,
         direction_flag] = line.strip().split(",")
        fnode_longitude, fnode_latitude, tnode_longitude, tnode_latitude, link_len = list(map(int,
                                                                                              [fnode_longitude,
                                                                                               fnode_latitude,
                                                                                               tnode_longitude,
                                                                                               tnode_latitude,
                                                                                               link_len]))
        G.addEdge(fnode_id, tnode_id, link_len)
        # 判断路径是否双向，是否添加其他边
        G.addEdge(tnode_id, fnode_id, link_len)

    return G

if __name__ == '__main__':
    G = read_data_piece('../data/dijkstra_test.CSV')
    source = G.getVertex('6')
    destination = G.getVertex('0')
    print(G.getVertices())
    print(G.getEdges())
    for obj in source.getConnections():
        print(obj.id)

