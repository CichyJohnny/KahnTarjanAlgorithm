class KahnAm:
    def __init__(self):
        self.am = []
        self.e = 0
        self.v = 0
        self.sorted = []
        self.not_visited = []
        self.in_degree = []

    # Create the adjacency matrix from user-console input
    def create_from_input(self):
        self.v = int(input("Enter the number of vertices: "))
        self.e = int(input("Enter the number of edges: "))
        self.am = [[0 for _ in range(self.v)] for _ in range(self.v)]

        self.in_degree = [0] * self.v
        self.not_visited = [True] * self.v
        for i in range(self.e):
            print("Enter the edge number ", i)
            a, b = map(int, input().split())
            self.am[a][b] = 1
            self.am[b][a] = -1
            self.in_degree[b] += 1

    # Create the adjacency matrix from a graph.txt file
    def create_from_file(self):
        with open("graph.txt") as f:
            self.v, self.e = map(int, f.readline().split())
            self.am = [[0 for _ in range(self.v)] for _ in range(self.v)]

            self.in_degree = [0] * self.v
            self.not_visited = [True] * self.v

            for i in range(self.e):
                a, b = map(int, f.readline().split())
                self.am[a][b] = 1
                self.am[b][a] = -1
                self.in_degree[b] += 1

    # Init method for Kahn's algorithm
    # Method returns the topological order of the graph or a message if the graph has a cycle
    def start(self):
        for i in range(self.v):
            if self.in_degree[i] == 0 and self.not_visited[i]:
                self.sorted.append(i)
                self.not_visited[i] = False

                next = []
                for j in range(self.v):
                    if self.am[i][j] == 1:
                        self.in_degree[j] -= 1
                        if self.in_degree[j] == 0 and self.not_visited[j]:
                            next.append(j)

                for j in next:
                    self.__kahn_go(j)

        for i in range(self.v):
            if self.not_visited[i]:
                self.sorted.append(i)

        if len(self.sorted) != self.v:
            return "The graph has a cycle"
        else:
            return '->'.join(map(str, self.sorted))

    # Recursive method for Kahn's algorithm
    def __kahn_go(self, k):
        self.sorted.append(k)
        self.not_visited[k] = False

        next = []
        for i in range(self.v):
            if self.am[k][i] == 1:
                self.in_degree[i] -= 1
                if self.in_degree[i] == 0 and self.not_visited[i]:
                    next.append(i)

        for i in next:
            self.__kahn_go(i)


if __name__ == "__main__":
    k = KahnAm()

    # k.create_from_input()
    k.create_from_file()

    print(k.start())
