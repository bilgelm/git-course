class Node():
    def __init__(self, data, neighbors: list["Node"] = []) -> None:
        self.data = data
        self.neighbors = neighbors
        self.visited = False
