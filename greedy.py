"""
Greedy algorithm
"""
import math
from graphs import generate_nodes


def greedy_alg(counter, time, tab, MAX_COST, THRESHOLD):

    items = [server.fit_results(time) for server in tab]

    server_cost = 0
    resource = 0

    #Jesli bierzemy tylko pod uwage koszt to

    if counter == "cost":
        items.sort(key=lambda x: x[1])
        print items

        while resource < THRESHOLD and server_cost <= MAX_COST:

            for i in range(len(items)):

                if server_cost + items[i][1] <= MAX_COST:

                    if resource + items[i][0] <= THRESHOLD:
                        server_cost += items[i][1]
                        resource += items[i][0]

                    if i == len(items) -1:
                        if resource + items[0][0] >= THRESHOLD:
                            server_cost += items[0][1]
                            resource += items[0][0]
                            break

                    elif resource + items[i+1][0] >= THRESHOLD:
                        server_cost += items[i+1][1]
                        resource += items[i+1][0]
                        break

        print server_cost
        print resource

    # Jesli bierzemy tylko pod uwage moc to
    if counter == "power":
        items.sort(key=lambda x: x[0])
        items.reverse()
        while resource < THRESHOLD and server_cost <= MAX_COST:

            for i in range(len(items)):

                if server_cost + items[i][1] <= MAX_COST:

                    if resource + items[i][0] <= THRESHOLD:
                        server_cost += items[i][1]
                        resource += items[i][0]

                    if i == len(items) - 1:
                        if resource + items[0][0] >= THRESHOLD:
                            server_cost += items[0][1]
                            resource += items[0][0]
                            break

                    elif resource + items[i + 1][0] >= THRESHOLD:
                        server_cost += items[i + 1][1]
                        resource += items[i + 1][0]
                        break

        print server_cost
        print resource

    # Jesli bierzemy pod uwage tylko koszt przez zasoby koszt/zasoby
    if counter == "divide":
        items.sort(key=lambda x: x[1]/(x[0] + 0.0))

        while resource < THRESHOLD and server_cost <= MAX_COST:

            for i in range(len(items)):

                if server_cost + items[i][1] <= MAX_COST:

                    if resource + items[i][0] <= THRESHOLD:
                        server_cost += items[i][1]
                        resource += items[i][0]

                    if i == len(items) - 1:
                        if resource + items[0][0] >= THRESHOLD:
                            server_cost += items[0][1]
                            resource += items[0][0]
                            break

                    elif resource + items[i + 1][0] >= THRESHOLD:
                        server_cost += items[i + 1][1]
                        resource += items[i + 1][0]
                        break

        print server_cost
        print resource

