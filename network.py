from heapq import heappush, heappop

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
    def add_node(self, nodeid):
        assert nodeid not in self._neighbours
        self._neighbours[nodeid] = []

    def remove_node(self, nodeid):
        assert nodeid in self._neighbours
        self._neighbours.pop(nodeid)

    def set_attribute(self, from_nodeid, to_nodeid, time=0, distance=0):
        assert from_nodeid in self._neighbours
        assert to_nodeid in self._neighbours
        assert to_nodeid in self._neighbours[from_nodeid]

        self._attributes['time'][(from_nodeid, to_nodeid)] = time
        self._attributes['distance'][(from_nodeid, to_nodeid)] = distance

    def add_link(self, from_nodeid, to_nodeid, time=0, distance=0):
        assert from_nodeid in self._neighbours
        assert to_nodeid in self._neighbours
        assert to_nodeid not in self._neighbours[from_nodeid]

        self._neighbours[from_nodeid].append(to_nodeid)
        self._attributes['time'].update({(from_nodeid, to_nodeid): time})
        self._attributes['distance'].update({(from_nodeid, to_nodeid): distance})

    def remove_link(self, from_nodeid, to_nodeid):
        assert from_nodeid in self._neighbours
        assert to_nodeid in self._neighbours
        assert to_nodeid in self._neighbours[from_nodeid]

        self._neighbours[from_nodeid].remove(to_nodeid)
        for attribute in self._attributes.values():
            del attribute[(from_nodeid, to_nodeid)]

    # 2. 查询
    def nodes(self):
        return list(self._neighbours.keys())

    def next_nodes(self, nodeid):
        return self._neighbours[nodeid]

    def prev_nodes(self, nodeid):
        prev_nodes_id = []
        for nodeid_ in self.nodes():
            if nodeid in self._neighbours[nodeid_]:
                prev_nodes_id.append(nodeid_)
        return prev_nodes_id

    def is_connected(self, from_nodeid, to_nodeid):
        if (to_nodeid in self._neighbours[from_nodeid]) or (from_nodeid in self._neighbours[to_nodeid]):
            return True
        else:
            return False

    def links(self):
        links = []

        for cur_node, next_nodes in self._neighbours.items():
            for next_node in next_nodes:
                links.append((cur_node, next_node))

        return links

    def show():
        # 可视化
        pass

    # 3. 属性
    def attributes(self, from_nodeid, to_nodeid):
        return {"time": self._attributes["time"][(from_nodeid, to_nodeid)], "distance": self._attributes["distance"][(from_nodeid, to_nodeid)]}

    def cost(self, from_nodeid, to_nodeid):
        self.attributes(from_nodeid, to_nodeid)["distance"]

    def shortest_route(self, od):
        origin, destination = od
        costs, routes = self.shortest_routes_from(origin)

        for route in routes:
            if routes[-1] == destination:
                return route

    # 4. 最短路径搜索
    def shortest_routes_from(self, nodeid):
        known = []
        unknow = []
        boundary = []
        prevs = {}
        costs = {}

        # 初始化
        for node in self.nodes():
            unknow.append(node)
            prevs[node] = None
            costs[node] = 10000000

        heappush(boundary, (0, nodeid))

        # 搜索循环
        while(boundary):
            cost, current_node = heappop(boundary)
            if current_node in known:
                continue
            known.append(current_node)
            costs[current_node] = cost

            for next_node in  self.next_nodes():
                new_cost = cost + self.cost(current_node, next_node)
                if new_cost < costs[next_node]:
                    prevs[next_node] = current_node
                    costs[next_node] = cost

                    heappush(boundary, (new_cost, next_node))

        # 重构路径
        routes = {}
        for node in self.nodes():
            routes[node] = None

        routes[nodeid] = [nodeid]

        while None in routes.values():
            for end_node, route in routes.items():
                if route is not None:
                    continue
                prev = prevs[end_node]
                if routes[prev] is not None:
                    routes[end_node] = routes[prev] + [end_node]

        return costs, routes

