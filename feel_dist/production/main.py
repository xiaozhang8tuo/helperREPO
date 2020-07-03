# codeing utf-8
'''
    author：mantou
    date: 2020.6
'''
from util.helper import Node

def load_linked_table(file_name):
    '''
    读取linked表，创建对应的节点和街道，并且返回对应的 node_dict 和 street_dict
    Args:
        file_name: linked表
    Return：
        node_dict: { key:node_id(str),   value: Node对象 }
    '''


    fp = open(file_name)
    line_num = 0
    node_dict = {}
    for line in fp:
        if line_num == 0:
            line_num += 1
            continue

        [link_id, fnode_id, fnode_longitude, fnode_latitude, tnode_id, tnode_longitude, tnode_latitude, link_len, direction_flag] = line.strip().split(",")
        fnode_longitude, fnode_latitude, tnode_longitude, tnode_latitude, link_len = list(map(int,
                                            [fnode_longitude, fnode_latitude, tnode_longitude, tnode_latitude, link_len]))

        print(link_id, fnode_id, fnode_longitude, fnode_latitude, tnode_id, tnode_longitude, tnode_latitude, link_len)

        # 创建or选取入度节点
        if fnode_id not in node_dict:
            f_node = Node(id=fnode_id, lat=fnode_latitude, long=fnode_longitude)
            node_dict[f_node.id] = f_node
        else:
            f_node = node_dict[fnode_id]

        # 创建or选取出度节点
        if tnode_id not in node_dict:
            t_node = Node(id=tnode_id, lat=tnode_latitude, long=tnode_longitude)
            node_dict[t_node.id] = t_node
        else:
            t_node = node_dict[tnode_id]

        # 入度节点的出度+1
        if t_node.id not in f_node.out_dict:
            f_node.set_outdeg(t_node, link_len)
        # 出度节点的入度+1
        if f_node.id not in t_node.out_dict:
            t_node.set_indeg(f_node, link_len)

        if direction_flag == '1':
            f_node.set_outdeg(t_node, link_len)
            t_node.set_indeg(f_node, link_len)

    fp.close()

    for id in node_dict:
        print(node_dict[id])
    return node_dict

def main_flow():
    load_linked_table()


if __name__ == '__main__':
    load_linked_table("../data/linded.csv")