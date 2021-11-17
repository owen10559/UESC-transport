from heapq import heappush, heappop
import matplotlib.pyplot as plt

class Node:
    def __init__(self, id:str='', x:float=.0, y:float=.0):
        self.id = id
        self.x = x
        self.y = y
        self.next_nodes = []

    def is_connect(self, other_node:'Node'):
        if other_node in self.next_nodes:
            return True
        else:
            return False

    def connect(self, other_node:'Node', bothway:bool=True):
        if not self.is_connect(other_node):
            self.next_nodes.append(other_node)
        if bothway:
            other_node.connect(self, bothway=False)#此处bothway必须设为false

    def disconnect(self, other_node:'Node', bothway:bool=True):
        if self.is_connect(other_node):
            self.next_nodes.remove(other_node)
        if bothway:
            other_node.disconnect(self, bothway=False)#此处bothway必须设为false

    def distance(self, other_node):
        if not self.is_connect(other_node):
            pass
        else:
            return ((self.x - other_node.x) ** 2 + (self.y - other_node.y) ** 2) ** (1/2)

    def get_prev_nodes(self, network:'Network'):
        prev_nodes = []
        for node in network.nodes:
            if self in node.next_nodes:
                prev_nodes.append(node)
        return prev_nodes

    def get_next_nodes(self):
        return self.next_nodes

class Network:
    def __init__(self, nodes:'list[Node]'=[]):
        self.nodes = nodes

    def add_node(self, node:'Node'):
        if node not in self.nodes:
            self.nodes.append(node)

    def remove_node(self, node:'Node'):
        if node in self.nodes:
            self.nodes.remove(node)

    def get_node(self, node_id:str):
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None

    def get_all_nodes(self):
        return self.nodes

    def connect(self, start_node:'Node', end_node:'Node', bothway:bool=True):
        if start_node in self.nodes and end_node in self.nodes:
            start_node.connect(end_node, bothway)

    def disconnect(self, start_node:'Node', end_node:'Node', bothway:bool=True):
        if start_node in self.nodes and end_node in self.nodes:
            start_node.disconnect(end_node, bothway)

    def gen_example(self):
        for id, x, y in [('A', 1, 1), ('B', 1.5, 3), ('C', 3, 2), ('D', 3, 4), ('E', 4, 3)]:
            self.add_node(Node(id, x, y))

        self.connect(self.nodes[0], self.nodes[1])
        self.connect(self.nodes[0], self.nodes[3])
        self.connect(self.nodes[1], self.nodes[3])
        self.connect(self.nodes[2], self.nodes[4])
        self.connect(self.nodes[0], self.nodes[2], bothway=False)
        self.connect(self.nodes[2], self.nodes[3], bothway=False)

    def show(self):
        plt.axis('equal')
        for node in self.nodes:
            plt.scatter(node.x, node.y, s=500,c='black')
            plt.text(node.x, node.y, node.id, c='white', fontsize=15, verticalalignment='center', horizontalalignment='center')
            for next_node in node.get_next_nodes():
                if node in next_node.get_next_nodes():
                    plt.plot([node.x, next_node.x], [node.y, next_node.y], linewidth=6, color='green', alpha=0.8)
                    plt.text((node.x + next_node.x)/2, (node.y + next_node.y)/2, '%.2fkm' % node.distance(next_node), fontsize=14, horizontalalignment='center')
                else:
                    dx = next_node.x - node.x
                    dy = next_node.y - node.y
                    plt.arrow(node.x, node.y, dx, dy, fc='green', alpha=0.8, width=0.07, head_width=0.15, head_length=0.4, length_includes_head=True)
                    plt.text((node.x + next_node.x)/2, (node.y + next_node.y)/2, '%.2fkm' % node.distance(next_node), fontsize=14, horizontalalignment='center')
        plt.show()
