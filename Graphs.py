# College Campus Graph using Adjacency Matrix

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[False] * vertices for _ in range(vertices)]

    def add_edge(self, source, destination):
        self.adj_matrix[source][destination] = True
        self.adj_matrix[destination][source] = True

    def display(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(1 if self.adj_matrix[i][j] else 0, end=" ")
            print()


g = Graph(6)
g.add_edge(0, 1)  # Main gate <-> Library
g.add_edge(0, 2)  # Main gate <-> Canteen
g.add_edge(1, 3)  # Library <-> Academic Block
g.add_edge(2, 3)  # Canteen <-> Academic Block
g.add_edge(3, 4)  # Academic Block <-> Hostel
g.add_edge(4, 5)  # Hostel <-> Sports Ground

g.display()

#  Library
#         /     \
#        /       \
#   Main Gate   Academic ------ Hostel ------- Sports Ground
#        \       /
#         \     /
#         Canteen

# 💡 Key differences: