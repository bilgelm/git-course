from node import Node

class Graph():
    # Directed acyclic graph
    node_list: list[Node]

    def __init__(self, node_list: list[Node] = []) -> None:
        self.node_list = node_list

    def unvisit(self) -> None:
        for node in self.node_list:
            node.visited = False

    def traverse(self) -> list:
        # depth-first traversal

        self.unvisit()
        output: list = []
        nbhr_list: list = []
        for node in self.node_list:
            nbhr_list.append(node)
            while nbhr_list:
                nbhr = nbhr_list.pop()
                if not nbhr.visited:
                    output.append(nbhr.data)
                    nbhr_list.extend(nbhr.neighbors)
                    nbhr.visited = True

        return output
