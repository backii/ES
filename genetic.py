"""
Genetic by MJ
"""

import random
from graphs import Server, Node, generate_nodes

HP = Server(1, 12, 3, 4, "HP")
IBM = Server(4, 5, 6, 7, "IBM")

tab1 = (HP, IBM)


class Genetic(object):

    def __init__(self):

        """
        Tworzymy rodzicow
        """

        self.all = generate_nodes(2, 5, 400, 10, tab1)
        self.servers = self.all.keys()
        self.values = self.all.values()
        self.parents = []
        for item in range(len(self.servers)):
            self.parents.append((self.servers[item], self.values[item]))
        self.parents.sort(key=lambda x: x[1])

    def crossover(self,  threshold, time):

            if len(self.parents) < 2:
                #raise IndexError("Empty array")
                return False

            list1 = self.parents[-1][0]
            list2 = self.parents[-2][0]

            parent1 = Node()
            parent1.server_tab = list1

            parent2 = Node()
            parent2.server_tab = list2

            index = random.randint(0, len(list2)-1)
            tmp_cross = parent1.server_tab[index]
            print tmp_cross

            """
                index = random.randint(0, len(parent1[0].server_tab))
                tmp_cross = parent1[0].server_tab[index]
                parent1[0].server_tab[index] = parent2[0].ser[index]
                parent2[index] = tmp_cross

                if parent1.calculate_all(time) >= threshold:
                    del self.parents[-2]
                    break

                elif parent2.calculate_all(time) >= threshold:
                    del self.parents[-1]
                    break
            print self.parents
            
            """

    def __mutate(self, node, tab1, threshold, time):

        while True:
            node.server_tab[random.randint(0, len(node.server_tab))] = random.choice(tab1)
            if node.calculate_all(time) >= threshold:
                break

    def generate(self):
        pass



new = Genetic()
print new.parents
new.crossover(100,10)
