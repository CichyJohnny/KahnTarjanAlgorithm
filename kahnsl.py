class KahnSl:
    def __init__(self):
        self.sl = {}
        self.e = 0
        self.v = 0
        self.sorted = []
        self.not_visited = []
        self.in_degree = []

    # Create the successor list from user-console input
    def create_from_input(self):
        self.v = int(input("Enter the number of vertices: "))
        self.e = int(input("Enter the number of edges: "))

        self.sl = {i: [[], []] for i in range(self.v)}
        self.not_visited = [True] * self.v

        for i in range(self.v):
            self.sl[i] = [[], []]

        for i in range(self.e):
            print("Enter the edge number ", i)
            a, b = map(int, input().split())

            self.sl[a][0].append(b)
            self.sl[b][1].append(a)

    # Create the successor list from a graph.txt file
    def create_from_file(self):
        with open("graph.txt") as f:
            self.v, self.e = map(int, f.readline().split())
            self.sl = {i: [[], []] for i in range(self.v)}

            self.not_visited = [True] * self.v
            self.in_degree = [0] * self.v

            for i in range(self.e):
                a, b = map(int, f.readline().split())

                self.sl[a][0].append(b)
                self.sl[b][1].append(a)
                self.in_degree[b] += 1

    # Init method for Kahn's algorithm
    def start(self):
        for key, val in self.sl.items():
            if val[0] and self.in_degree[key] == 0 and self.not_visited[key]:
                self.__kahn_go(key)

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

        for val in self.sl[k][0]:
            self.in_degree[val] -= 1

        for next_k in self.sl[k][0]:
            if self.in_degree[next_k] == 0 and self.not_visited[next_k]:
                self.__kahn_go(next_k)


if __name__ == "__main__":
    k = KahnSl()

    # k.create_am_from_input()
    k.create_from_file()

    print(k.start())
