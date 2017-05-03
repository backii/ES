"""
Main function for statistics only.
Just for functions executions only!!!
"""

from graphs import Server, Node

HP = Server(1,2,3)
IBM = Server(2,3,4)
LENOVO = Server(4,5,6)
SERVERS = [HP,IBM,LENOVO]

new = Node()
new.generate(SERVERS, 5)
