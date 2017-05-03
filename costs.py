"""
Generate nodes which fits the limits
"""
from graphs import Node
import random

def fit(work, time, servers, size):
    nodes = list()
    while True:
        tmp = Node()
        tmp.generate(servers, size)
        work_sum = 0
        for node in tmp.get_node():
            time = random.randint(1, time)
            work_sum = tmp.calculate(time)

        if work_sum >= work:
            nodes.append(tmp)
        if len(nodes) == 10:
            break

