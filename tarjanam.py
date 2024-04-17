class TarjanAm:
    def __init__(self):
        self.am = []
        self.e = 0
        self.v = 0
        self.sorted = []
        self.count = 0
        self.cycle = False

    def create_am_from_input(self):
        self.v = int(input("Enter the number of vertices: "))
        self.e = int(input("Enter the number of edges: "))
        self.am = [[0 for _ in range(self.v)] for _ in range(self.v)]

        for i in range(self.e):
            print("Enter the edge number ", i)
            a, b = map(int, input().split())
            self.am[a][b] = 1
            self.am[b][a] = -1

    def create_am_from_file(self):
        with open("graph.txt") as f:
            self.v, self.e = map(int, f.readline().split())
            self.am = [[0 for _ in range(self.v)] for _ in range(self.v)]

            for i in range(self.e):
                a, b = map(int, f.readline().split())
                self.am[a][b] = 1
                self.am[b][a] = -1

    def tarjan_start(self, start=-1):
        visited = [False] * self.v
        stack_member = [False] * self.v

        if start != -1:
            self.tarjan_go(start, visited, stack_member)

        for i in range(self.v):
            if not visited[i]:
                self.tarjan_go(i, visited, stack_member)
                if self.cycle:
                    break

        if not self.cycle:
            print('->'.join(map(str, self.sorted[::-1])))
        else:
            print("The graph has a cycle")

    def tarjan_go(self, i, visited, stack_member):
        visited[i] = True
        stack_member[i] = True

        for j in range(self.v):
            if self.am[i][j] == 1:
                if not visited[j]:
                    self.tarjan_go(j, visited, stack_member)
                elif stack_member[j]:
                    self.cycle = True
                    return

        self.sorted.append(i)
        stack_member[i] = False


if __name__ == "__main__":
    k = TarjanAm()

    # k.create_am_from_input()
    k.create_am_from_file()

    k.tarjan_start(7)
