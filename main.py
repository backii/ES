"""
Main function for statistics only.
Just for functions executions only!!!
"""
from graphs import Server, generate_nodes
from genetic import Genetic


SERVERS = {
            "Serwer HP ProLiant ML350 gen9": (16, 1, 8, 0.65*0.5, "Serwer HP ProLiant ML350 gen9"),
            "Serwer Fujitsu RX2520 M1": (8, 1, 4, 0.65*0.45, "Serwer Fujitsu RX2520 M1"),
            "Serwer IBM System x3550 M5": (16, 2, 10, 0.7*0.55, "Serwer IBM System x3550 M5"),
            "Serwer Lenovo ThinkServer RD650": (8, 2, 6, 0.65*0.75, "Serwer Lenovo ThinkServer RD650"),
            "Serwer DELL T430 z CPU Xeon 8C": (8, 2, 8, 0.65*0.75, "Serwer DELL T430 z CPU Xeon 8C"),
}
"""
Ok zioemczki przyjmiemy dla latwosci, ze kompy sa obciazone w 80 % 
Zasilacz na straty cieplne i inne pierdy traci 15% wiec od mocy zsilacza musimy dojac 35% i mamy pobor 
"""

HP = Server(SERVERS["Serwer HP ProLiant ML350 gen9"][0], SERVERS["Serwer HP ProLiant ML350 gen9"][1],
            SERVERS["Serwer HP ProLiant ML350 gen9"][2], SERVERS["Serwer HP ProLiant ML350 gen9"][3],
            "Serwer HP ProLiant ML350 gen9")

FUJITSU = Server(SERVERS["Serwer Fujitsu RX2520 M1"][0], SERVERS["Serwer Fujitsu RX2520 M1"][1],
            SERVERS["Serwer Fujitsu RX2520 M1"][2], SERVERS["Serwer Fujitsu RX2520 M1"][3],
            "Serwer Fujitsu RX2520 M1")

IBM = Server(SERVERS["Serwer IBM System x3550 M5"][0], SERVERS["Serwer IBM System x3550 M5"][1],
            SERVERS["Serwer IBM System x3550 M5"][2], SERVERS["Serwer IBM System x3550 M5"][3],
             "Serwer IBM System x3550 M5")

LENOVO = Server(SERVERS["Serwer Lenovo ThinkServer RD650"][0], SERVERS["Serwer Lenovo ThinkServer RD650"][1],
            SERVERS["Serwer Lenovo ThinkServer RD650"][2], SERVERS["Serwer Lenovo ThinkServer RD650"][3],
                "Serwer Lenovo ThinkServer RD650")

DELL = Server(SERVERS["Serwer DELL T430 z CPU Xeon 8C"][0], SERVERS["Serwer DELL T430 z CPU Xeon 8C"][1],
            SERVERS["Serwer DELL T430 z CPU Xeon 8C"][2], SERVERS["Serwer DELL T430 z CPU Xeon 8C"][3],
                "Serwer DELL T430 z CPU Xeon 8C")

tab_servers = (HP, FUJITSU, IBM, LENOVO, DELL)

new = Genetic(3,4,1000,10,tab_servers)
new.generate(1000,10,tab_servers)
print new.parents