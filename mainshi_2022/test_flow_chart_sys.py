# coding = utf-8
"""
流程管理系统  来自3ms
[
'FlowChartSys', 'add_node', add_node', add_node', 'add_conn', 'add_node', 'query'
'rm_node', 'rm_conn'
]
[
[], [100, 0], [101, 0], [102, 1], [20, 100, 101], [105, 1], [100], [101], [20]
]
"""
class FlowChartSys:
    def __init__(self):
        self.nodes = {}   # {'node_id': 'node_type'}
        self.conns = {}

    def add_node(self, node):
        """增加节点
        1-普通节点
        2-中继节点 与其他节点自动建立连接
        """
        node_val, node_type = node
        if node_val in self.nodes:
            return False
        self.nodes.setdefault(node_val, node_type)
        return True

    def add_conn(self, conn):
        """增加连接"""
        # [20, 100, 101]
        conn_id, start_node_id, end_node_id = conn
        if conn_id in self.conns:
            return False
        if start_node_id == end_node_id:
            return False
        self.conns.setdefault(conn_id, [start_node_id, end_node_id])
        return True

    def rm_conn(self, conn_id):
        """移除链接"""
        if conn_id in self.conns:
            self.conns.pop(conn_id)
            return True
        return False

    def rm_node(self, node_id):
        """移除node"""
        if node_id not in self.nodes:
            return False
        import copy
        new_conns = copy.deepcopy(self.conns)
        for conn_id, conn_val in list(self.conns.items()):
            if node_id not in conn_val:
                continue
            new_conns.pop(conn_id)
        self.conns = new_conns
        self.nodes.pop(node_id)
        return True

    @staticmethod
    def query_one(conns, is_queryed_conns, node_id):
        for conn_id, conn_val in list(conns.items()):
            if conn_id in is_queryed_conns:
                continue
            is_queryed_conns.append(conn_id)
            if node_id != conn_val[0]:
                continue

    def query(self, node_id):
        """查找以node_id为起点的所有链接， 包括自动和手动的
        返回这些链接的终点(不是计算最终的终点，计算直接链接的终点)列表（去重在升序），
        若node不存在或无连接，返回空[]
        """
        if node_id not in self.nodes:
            return []
        # 手工创建的连接
        conns = [i for i in list(self.conns.values())]
        end_node_list = []
        for node_start, node_end in conns:
            if node_start != node_id:
                continue
            end_node_list.append(node_end)
        end_node_list.extend([i for i, j in list(self.nodes.items()) if j == 1])
        return list(set(end_node_list))


if __name__ == '__main__':
    f = FlowChartSys()
    """[
'FlowChartSys', 'add_node', add_node', add_node', 'add_conn', 'add_node', 'query'
'rm_node', 'rm_conn'
]"""
    """[], [100, 0], [101, 0], [102, 1], [20, 100, 101], [105, 1], [100], [101], [20]"""
    f.add_node([100, 0])
    f.add_node([101, 0])
    f.add_node([102, 1])
    f.add_conn([20, 100, 101])
    f.add_node([105, 1])
    print((f.query(100)))
    f.rm_node(101)
    f.rm_conn(20)
    print((f.nodes))
    print((f.conns))








