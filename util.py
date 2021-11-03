class FlowBundle:
    def __init__(self):
        self.flows = []

    def add_flow(self, route, flow):
        self.flows.append((route, flow))

class FlowMap:
    def __init__(self, network, default_flow=0.0):
        self.flows = {}

        for link in network.links():
            self.flows[link] = default_flow

    def update(self, link, flow):
        self.flows[link] = flow

    def accumulate(self, link, flow):
        self.flows[link] += flow

    def clear(self):
        for link in self.flows.keys():
            self.flows[link] = 0.0

def bundle_to_map(map, bundle):
    for route, flow in bundle.flows:
        links = route_to_links(route)
        for link in links:
            map.accumulate(link, flow)

def route_to_links(route):
    route = list(route)
    links = []
    for link in zip(route[:-1], route[1:]):
        links.append(link)

    return links