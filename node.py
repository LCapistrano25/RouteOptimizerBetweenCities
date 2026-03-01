class Node:
    def __init__(self, content):
        self.content = content
        self.neighbors = {}

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost

    def __lt__(self, other):
        return self.content < other.content
