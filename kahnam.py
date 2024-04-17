class KahnAm:
    def __init__(self):
        self.am = []
        self.e = 0
        self.v = 0
        self.sorted = []

    def create_am_from_input(self):
        self.v = int(input("Enter the number of vertices: "))
        self.e = int(input("Enter the number of edges: "))
        self.am = [[0 for _ in range(self.e)] for _ in range(self.e)]

        for i in range(self.e):
            print("Enter the edge number ", i)
            a, b = map(int, input().split())
            self.am[a][b] = 1
            self.am[b][a] = -1

    def create_am_from_file(self):
        with open("graph.txt") as f:
            self.v, self.e = map(int, f.readline().split())
            self.am = [[0 for _ in range(self.e)] for _ in range(self.e)]

            for i in range(self.e):
                a, b = map(int, f.readline().split())
                self.am[a][b] = 1
                self.am[b][a] = -1

    def kahn_start(self):
        for i in range(self.e):
            if -1 not in self.am[i]:
                for j in range(self.e):
                    if self.am[i][j] == 1:
                        self.sorted.append(i)
                        self.kahn_go(i, j)

        if len(self.sorted) != self.v:
            print("The graph has a cycle")
        else:
            print('->'.join(map(str, self.sorted)))

    def kahn_go(self, i, j):
        for k in range(self.e):
            self.am[i][k] = 0
            self.am[k][i] = 0

        if -1 not in self.am[j]:
            self.sorted.append(j)
            for k in range(self.e):
                if self.am[j][k] == 1:
                    self.kahn_go(j, k)


if __name__ == "__main__":
    k = KahnAm()

    # k.create_am_from_input()
    k.create_am_from_file()

    k.kahn_start()
