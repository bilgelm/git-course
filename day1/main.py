from node import Node
from graph import Graph

n4 = Node(4)
n3 = Node(3, [n4])
n2 = Node(2, [n3])
n7 = Node(7)
n6 = Node(6, [n7])
n8 = Node(8)
n5 = Node(5, [n6, n8])
n10 = Node(10)
n9 = Node(9, [n10])
n1 = Node(1, [n2, n5, n9])

grph = Graph([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10])

print(grph.traverse())