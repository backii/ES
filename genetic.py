"""
Genetic by MJ
"""

import random
from graphs import Server, Node, generate_nodes

HP = Server(1, 12, 3, 4, "HP")
IBM = Server(4, 5, 6, 7, "IBM")

tab1 = (HP, IBM)


class Genetic(object):

    def __init__(self, graph_size, node_size, threshold, time):

        """
        Tworzymy rodzicow
        """

        self.all = generate_nodes(graph_size, node_size, threshold, time, tab1)
        self.servers = self.all.keys()
        self.values = self.all.values()
        self.parents = []
        for item in range(len(self.servers)):
            self.parents.append((self.servers[item], self.values[item]))
        self.parents.sort(key=lambda x: x[1])

    def crossover(self,  threshold, time):

            list1 = self.parents[-1][0]
            list2 = self.parents[-2][0]

            parent1 = Node()
            parent1.server_tab = list(list1)

            parent2 = Node()
            parent2.server_tab = list(list2)

            while True:

                index = random.randint(0, len(list2)-1)
                tmp_cross = parent1.server_tab[index]
                parent1.server_tab[index] = parent2.server_tab[index]
                parent2.server_tab[index] = tmp_cross

                if parent2.calculate_all(time) >= threshold:
                    del self.parents[-1]
                    break

                elif parent1.calculate_all(time) >= threshold:
                    del self.parents[-2]
                    break

            self.parents.sort(key=lambda x: x[1])
            print self.parents

    @staticmethod
    def mutate(node, tab1, threshold, time):

        tmp_node = node
        while True:

            node.server_tab[random.randint(0, len(node.server_tab)-1)] = random.choice(tab1)

            if node.calculate_all(time) >= threshold:
                if node.calculate_all(time) >= tmp_node.calculate_all(time):
                    break

    def generate(self, threshold, time):
        """ Do mutate and crossover again till I die """

        while len(self.parents) >= 2:
            self.crossover(threshold, time)

        for nodes in self.parents:
            node = Node()
            node.server_tab = list(nodes[0])
            self.mutate(node, tab1, threshold, time)
