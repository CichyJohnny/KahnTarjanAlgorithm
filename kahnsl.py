class KahnSl:
    def __init__(self):
        self.sl = {}
        self.e = 0
        self.v = 0
        self.sorted = []

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

    def kahn_start(self):
        for key, val in self.sl.items():
            if not val[1] and val[0]:
                self.kahn_go(key)

        if len(self.sorted) != self.v:
            print("The graph has a cycle")
        else:
            print('->'.join(map(str, self.sorted)))

    def kahn_go(self, k):
        self.sorted.append(k)

        for key, val in self.sl.items():
            if k in val[0]:
                val[0].remove(k)
            if k in val[1]:
                val[1].remove(k)

        for next_k in self.sl[k][0]:
            if not self.sl[next_k][1]:
                self.kahn_go(next_k)



if __name__ == "__main__":
    k = KahnSl()

    # k.create_am_from_input()
    k.create_sl_from_file()

    k.kahn_start()
