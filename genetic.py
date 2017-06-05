"""
Genetic by MJ
"""

"""
Fittness - minimum costs
"""


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

    def crossover(self):

        pass

    def __mutate(self):
        pass


new = Genetic()
print new.parents
