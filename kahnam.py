class KahnAm:
    def __init__(self):
        self.am = []
        self.e = 0
        self.v = 0
        self.sorted = []

    # Create the adjacency matrix from user-console input
    def create_from_input(self):
        self.v = int(input("Enter the number of vertices: "))
        self.e = int(input("Enter the number of edges: "))
        self.am = [[0 for _ in range(self.v)] for _ in range(self.v)]

        for i in range(self.e):
            print("Enter the edge number ", i)
            a, b = map(int, input().split())
            self.am[a][b] = 1
            self.am[b][a] = -1

    # Create the adjacency matrix from a graph.txt file
    def create_from_file(self):
        with open("graph.txt") as f:
            self.v, self.e = map(int, f.readline().split())
            self.am = [[0 for _ in range(self.v)] for _ in range(self.v)]

            for i in range(self.e):
                a, b = map(int, f.readline().split())
                self.am[a][b] = 1
                self.am[b][a] = -1

    # Init method for Kahn's algorithm
    # Method returns the topological order of the graph or a message if the graph has a cycle
    def start(self):
        for i in range(self.v):
            if -1 not in self.am[i]:
                for j in range(self.v):
                    if self.am[i][j] == 1:
                        self.sorted.append(i)
                        self.__kahn_go(i, j)

        if len(self.sorted) != self.v:
            return "The graph has a cycle"
        else:
            return '->'.join(map(str, self.sorted))

    # Recursive method for Kahn's algorithm
    def __kahn_go(self, i, j):
        for k in range(self.v):
            self.am[i][k] = 0
            self.am[k][i] = 0

        if -1 not in self.am[j]:
            self.sorted.append(j)
            for k in range(self.v):
                if self.am[j][k] == 1:
                    self.__kahn_go(j, k)


if __name__ == "__main__":
    k = KahnAm()

    # k.create_am_from_input()
    k.create_from_file()

    print(k.start())
