class TarjanSl:
    def __init__(self):
        self.sl = {}
        self.e = 0
        self.v = 0
        self.sorted = []
        self.count = 0
        self.cycle = False

    def create_sl_from_input(self):
        self.v = int(input("Enter the number of vertices: "))
        self.e = int(input("Enter the number of edges: "))

        for i in range(self.e):
            print("Enter the edge number ", i)
            a, b = map(int, input().split())

            if a not in self.sl.keys():
                self.sl[a] = [[], []]
            if b not in self.sl.keys():
                self.sl[b] = [[], []]

            self.sl[a][0].append(b)
            self.sl[b][1].append(a)

    def create_sl_from_file(self):
        with open("graph.txt") as f:
            self.v, self.e = map(int, f.readline().split())
            for i in range(self.e):
                a, b = map(int, f.readline().split())

                if a not in self.sl.keys():
                    self.sl[a] = [[], []]
                if b not in self.sl.keys():
                    self.sl[b] = [[], []]

                self.sl[a][0].append(b)
                self.sl[b][1].append(a)

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

        for j in self.sl[i][0]:
            if not visited[j]:
                self.tarjan_go(j, visited, stack_member)
            elif stack_member[j]:
                self.cycle = True
                return

        self.sorted.append(i)
        stack_member[i] = False


if __name__ == "__main__":
    k = TarjanSl()

    # k.create_sl_from_input()
    k.create_sl_from_file()

    k.tarjan_start(7)
