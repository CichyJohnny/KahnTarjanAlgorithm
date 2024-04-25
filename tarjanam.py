class TarjanAm:
    def __init__(self):
        self.am = []
        self.e = 0
        self.v = 0
        self.sorted = []
        self.count = 0
        self.cycle = False
        self.not_visited = []
        self.stack_member = []

    # Create the adjacency matrix from user-console input
    def create_from_input(self):
        self.v = int(input("Enter the number of vertices: "))
        self.e = int(input("Enter the number of edges: "))
        self.am = [[0 for _ in range(self.v)] for _ in range(self.v)]

        self.not_visited = [False] * self.v
        self.stack_member = [False] * self.v

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

            self.not_visited = [True] * self.v
            self.stack_member = [False] * self.v

            for i in range(self.e):
                a, b = map(int, f.readline().split())
                self.am[a][b] = 1
                self.am[b][a] = -1

    # Init method for Tarjan's algorithm
    def start(self, start=-1):
        stack_member = [False] * self.v

        if start != -1:
            self.__tarjan_go(start, stack_member)

        for i in range(self.v):
            if self.not_visited[i]:
                self.__tarjan_go(i, stack_member)

                if self.cycle:
                    break

        if not self.cycle:
            self.sorted.reverse()  # Reversing the order
            return '->'.join(map(str, self.sorted))
        else:
            return "The graph has a cycle"

    # Recursive method for Tarjan's algorithm
    def __tarjan_go(self, i, stack_member):
        self.not_visited[i] = False
        stack_member[i] = True

        for j in range(self.v):
            if self.am[i][j] == 1:
                if self.not_visited[j]:
                    self.__tarjan_go(j, stack_member)
                elif stack_member[j]:
                    self.cycle = True
                    return

        self.sorted.append(i)  # Change here
        stack_member[i] = False


if __name__ == "__main__":
    k = TarjanAm()

    # k.create_am_from_input()
    k.create_from_file()

    print(k.start())
