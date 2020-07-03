import operator
import math

class Node:
    def __init__(self, id='0', lat=0, long=0):
        self.id = id
        self.in_deg = 0
        self.in_dict = {}             # dict {key:Node.id, value:distance}
        self.out_deg = 0
        self.out_dict = {}            # dict {key:Node.id, value：distance}
        self.lat = lat
        self.long = long

    # 设置节点的出度
    def set_outdeg(self, t_node, f_t_dist):
        self.out_deg += 1
        self.out_dict.setdefault(t_node.id, 0)
        self.out_dict[t_node.id] = f_t_dist

    # 设置节点的入度
    def set_indeg(self, f_node, f_t_dist):
        self.in_deg += 1
        self.in_dict.setdefault(f_node.id, 0)
        self.in_dict[f_node.id] = f_t_dist

    def __str__(self):

        # print(self.id)
        # print(self.in_deg)
        in_ = []
        for zhuhe in sorted(self.in_dict.items(), key=operator.itemgetter(1)):
            in_.append(str(zhuhe[0]) + ":" + str(zhuhe[1]))

        out_ = []
        for zhuhe in sorted(self.out_dict.items(), key=operator.itemgetter(1)):
            out_.append(str(zhuhe[0]) + ":" + str(zhuhe[1]))

        return 'id:'+str(self.id) \
               + ' 入度:' + str(self.in_deg) \
               + " 入度节点:{" + ", ".join(in_) + "}" \
               + ' 出度:' + str(self.out_deg) \
               + " 出度节点:{" + ", ".join(out_) + "}"


def get_distance(self, lat1,lng1,lat2,lng2):
    dx = lng1 - lng2
    dy = lat1 - lat2
    b = (lat1 + lat2) / 2.0
    Lx = math.radians(dx) * 6367000.0* math.cos(math.radians(b))
    Ly = 6367000.0 * math.radians(dy)
    return math.sqrt(Lx * Lx + Ly * Ly)

if __name__ == '__main__':
    print(Node(id=1, lat=2, long=2))
