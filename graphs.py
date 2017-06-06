"""
Generate and bulid graphs from scratch

"""

import random

COST = 0.54


class Server(object):

    """
    Server with calculate funtion to show cost_power and resources like ram
    """

    def __init__(self, ram, proc, cores, power_supply, name):

        self.ram = ram
        self.proc = proc
        self.cores = cores
        self.power_supply = power_supply
        self.name = name

    def __str__(self):

        return "Server with params ram:{0}, procesor:{1}, cores:{2}. power consumption:{3} and name:{4}".format(self.ram,
                                                                                                                self.proc,
                                                                                                                self.cores,
                                                                                                                self.power_supply,
                                                                                                                self.name)

    def __claculate(self):
        """
        Calculate resources
        """
        return self.ram*self.proc*self.cores

    def __calculate_cost(self, time):
        """
        calculate all costs
        """
        return round(COST*self.power_supply*time, 3)

    def fit_results(self, time):
        """
        Show results
        """
        return self.__claculate(), self.__calculate_cost(time)


class Node(object):
    """
    Node consists of several different servers, saved in the array
    """

    def __init__(self):

        self.server_tab = []

    def add_server(self, server):

        self.server_tab.append(server)

    def calculate_all(self, time):

        return sum([server.fit_results(time)[0] for server in self.server_tab])

    def all_cost(self, time):

        return sum([server.fit_results(time)[1] for server in self.server_tab])

    def __str__(self):
        return "Node consists of {0}".format(self.server_tab)


"""
Generujemy sobie np 5 nodow spelniajacych okreslone warunki na prace tzn w szczegolnosci ogranicza nasz czas
i w tym czasie funkcja calculate dla sumy wszystkich nodow musi byc wieksza lub rowna naszej przyjetej wartosci :D
a w Nodzie np ma byc 4 serverow, kazdy node to rozwiazanie funkcji celu, czyli losujemy 5 rozwiazan
"""


def generate_nodes(graph_size, node_size, threshold, time, tab1,  tmp=Node()):

    nodes_list = []

    dict_with_results = {}

    while len(nodes_list) < graph_size:

        for i in range(node_size):
            server = random.choice(tab1)
            tmp.add_server(server)

        if tmp.calculate_all(time) >= threshold and tmp.all_cost(time) not in dict_with_results.values():

            nodes_list.append(tmp)
            dict_with_results[tuple(tmp.server_tab)] = tmp.all_cost(time)

        tmp.server_tab = []

    return dict_with_results


"""
TO DO
2. Implementacja Grafu / drzewa - struktura noda jest wystarczy  dodac klase drzewko i git majonez walczymy o cos
3. BFS
4. Greedy
5. Tabu search moze ktos sie podejmie
6. wyniki porownanie algorytmow
7. Trzeba sie zastanowic jakie dane wrzucamy do przemielenia zeby te nody nam sie jakos losowaly ok
"""