"""
Generate and bulid graphs from scratch

"""
import random


class Server(object):
    """
    Class node with needed arguments like watts, ram, processor.
    """
    def __init__(self, proc, ram, core):
        """
        :param proc:
        :param ram:
        :param core:
        """
        self.core = core
        self.ram = ram
        self.proc = proc

    def calculate(self, time):
        """
        :param time:
        :param work:
        :return:
        """
        return time*self.proc*self.core*self.ram


class Node(Server):

    def __init__(self):
        self.node = list()
        self.root = False

    def generate(self, servers, size):

        nodes = []
        for i in range(0, size):
            nodes.append(random.choice(servers))
        self.node = nodes

    def get_node(self):

        return self.node

class Graph(object):

    def __init__(self):
        self.nodes = []
        #self.root = self.nodes[0]
        self.graph = {}
        self.edges = []

    def add_edge(self, input, output):
            self.edges.append((input, output))

    def add_node(self, node):

        self.nodes.append(node)

    def generate_graph(self):

        for node in self.nodes:
            self.graph[node] = []
            for edge in self.edges:
                if node == edge[0]:
                    self.graph[node].append(edge[1])
