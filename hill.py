"""
Hill Climbing
"""

def hill_climbing(tab, MAX_COST):

    servers = tab.keys()
    costs = tab.values()

    current_node = servers[0]
    i = 0

    while True:

        if i < len(servers) - 2:

            neighbors = servers[i+1:i+3]
            next_neigbor_cost = 99999999999999
            next_node = None

            for neighbor in neighbors:

                neighbor_cost = costs[servers.index(neighbor)]

                if neighbor_cost < next_neigbor_cost:
                    next_neigbor_cost = neighbor_cost
                    next_node = neighbor
            i += 3

        elif len(servers) -1 >= i >= len(servers) -2:

            neighbor = servers[i+1]
            neighbor_cost = costs[i+1]
            
            if neighbor_cost < next_neigbor_cost:
                next_neigbor_cost = neighbor_cost
                next_node = neighbor

            i += 1

        neighbor_cost = costs[servers.index(current_node)]

        if neighbor_cost <= next_neigbor_cost and neighbor_cost < MAX_COST:
            return current_node, neighbor_cost

        current_node = next_node

