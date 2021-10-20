class Network:
    def __init__(self):
        self._neighbours = {}
        self._attributes = {}

    def make_example(self):
        self._neighbours = {
            "A": ["B", "C", "D"],
            "B": [],
            "C": [],
            "D": ["B"]
        }

        self._attributes = {
            "time": {
                ("A", "B"): 23,
                ("A", "C"): 34,
                ("A", "D"): 26,
                ("D", "B"): 17
            },

            "distance": {
                ("A", "B"): 230,
                ("A", "C"): 340,
                ("A", "D"): 260,
                ("D", "B"): 170
            },
        }
    # 1. 增删查改
    def add_node(self):
        None

    def remove_node(self, nodeid):
        None

    def add_link(self, from_nodeid, to_nodeid):
        None

    def remove_link(self, from_nodeid, to_nodeid):
        None

    # 2. 查询
    def from_nodes(self, nodeid):
        None

    def to_nodes(self, nodeid):
        None

    def is_connected(self, from_nodeid, to_nodeid):
        None

    # 3. 属性
    def attributes(self, from_nodeid, to_nodeid):
        None

    # 4. 最短路径搜索
    def shortest_routes_from(self, nodeid):
        None