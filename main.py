class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []
        self.parent = [-1] * num_vertices

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def find(self, i):
        if self.parent[i] == -1:
            return i
        return self.find(self.parent[i])

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        self.parent[u_root] = v_root

    def kruskal_mst(self):
        result = []
        sorted_edges = sorted(self.edges, key=lambda x: x[2])
        for u, v, weight in sorted_edges:
            if self.find(u) != self.find(v):
                self.union(u, v)
                result.append((u, v, weight))
        return result

    def reverse_edges(self):
        reversed_edges = [(v, u, -w) for u, v, w in self.edges]
        self.edges = reversed_edges

    def kruskal_max_st(self):
        self.reverse_edges()
        max_st = self.kruskal_mst()
        self.reverse_edges()
        return max_st

# Зчитування матриці суміжності з файлу
with open("input.txt", "r") as file:
    matrix = [list(map(int, line.strip().split())) for line in file.readlines()]

# Створення графу та додавання ребер
g = Graph(len(matrix))
for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        if matrix[i][j] != 0:
            g.add_edge(i, j, matrix[i][j])

mst = g.kruskal_mst()
min_weight = sum([weight for _, _, weight in mst])
print("Мінімальне остове дерево:")
for u, v, weight in mst:
    print(f"({u}, {v}), вага: {weight}")
print(f"Сума ваг мінімального остового дерева: {min_weight}\n")


