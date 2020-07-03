# code-utf8
from util.Graph_and_Vertex_v1 import Graph
from util.Graph_and_Vertex import Vertex
import json
from util.Graph_and_Vertex_v1 import Graph
from util.Graph_and_Vertex_v1 import Vertex

def read_data_piece(file_name):
    '''
        读取linked表(csv)，创建对应的节点和街道，并且返回对应的 node_dict 和 street_dict
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


        [link_id, fnode_id, f_loc, fnode_longitude, fnode_latitude, tnode_id, t_loc, tnode_longitude, tnode_latitude, link_len,
         direction_flag] = line.strip().split(",")
        fnode_longitude, fnode_latitude, tnode_longitude, tnode_latitude, link_len = list(map(float,
                                                                                              [fnode_longitude,
                                                                                               fnode_latitude,
                                                                                               tnode_longitude,
                                                                                               tnode_latitude,
                                                                                               link_len]))
        G.addEdge(fnode_id, f_loc, tnode_id, t_loc, link_len)
        # 判断路径是否双向，是否添加其他边
        G.addEdge(tnode_id, t_loc, fnode_id, f_loc, link_len)
    return G

def read_json(jsonlist):
    """

    :param jsonlist: 保存图的list格式文件  json。loads(）的返回文件
    :return: 图
    """
    G = Graph(True)
    for v in jsonlist:  # {'id': '5', 'loc': '3_3', 'adjacent': [{'adj_id': '1', 'loc': '3_3', 'weight': 2.5}, {'adj_id': '2', 'loc': '3_3', 'weight': 1.5}]}
        for adj in v["adjacent"]: # {'adj_id': '1', 'loc': '4_2', 'weight': 3.0}
            # print(adj)
            G.addEdge(v['id'], v['loc'], adj['adj_id'], adj['loc'], adj["weight"])
    G.numVertices = len(G.vertDictionary)
    return G






if __name__ == '__main__':
    G =read_data_piece("../data/dijkstra_A.CSV")
    g_json = G.toJson()
    a = json.loads(g_json)
    G1 = read_json(a)
    print(G1.numVertices)



    ################################################
    # G = read_data_piece('../data/dijkstra_A.CSV')
    # source = G.getVertex('17')
    # destination = G.getVertex('18')
    # print(G.getVertices())
    # print(G.getEdges())
    # # for obj in source.getConnections():
    # #     print(obj)
    #
    # for obj in G.vertDictionary.values():
    #     print(obj)

