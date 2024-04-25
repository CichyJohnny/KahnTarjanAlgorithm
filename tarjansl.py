class TarjanSl:
    def __init__(self):
        self.sl = {}
        self.e = 0
        self.v = 0
        self.sorted = []
        self.count = 0
        self.cycle = False
        self.not_visited = []

    # Create the successor list from user-console input
    def create_from_input(self):
        self.v = int(input("Enter the number of vertices: "))
        self.e = int(input("Enter the number of edges: "))

        for i in range(self.v):
            self.sl[i] = [[], []]

        self.not_visited = [True] * self.v

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

            for i in range(self.e):
                a, b = map(int, f.readline().split())

                self.sl[a][0].append(b)
                self.sl[b][1].append(a)

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
            return '->'.join(map(str, self.sorted[::-1]))
        else:
            return "The graph has a cycle"

    # Recursive method for Tarjan's algorithm
    def __tarjan_go(self, i, stack_member):
        self.not_visited[i] = False
        stack_member[i] = True

        for j in self.sl[i][0]:
            if self.not_visited[j]:
                self.__tarjan_go(j, stack_member)
            elif stack_member[j]:
                self.cycle = True
                return

        self.sorted.append(i)
        stack_member[i] = False


if __name__ == "__main__":
    k = TarjanSl()

    # k.create_sl_from_input()
    k.create_from_file()

    print(k.start())
