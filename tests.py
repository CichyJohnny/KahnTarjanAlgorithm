from kahnam import KahnAm
from kahnsl import KahnSl
from tarjanam import TarjanAm
from tarjansl import TarjanSl

import random
import time
import copy
import matplotlib.pyplot as plt
import numpy as np


# Random DAG generator returns a successor list and the number of edges
def rand_dag_successor(n, p):
    successor_list = {i: [[], []] for i in range(n)}
    num_edges = 0

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                successor_list[i][0].append(j)
                successor_list[j][1].append(i)

                num_edges += 1

    return successor_list, num_edges


# Random DAG generator returns an adjacency matrix and the number of edges
def rand_dag_adjacency(n, p):
    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
    num_edges = 0

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                adjacency_matrix[i][j] = 1
                adjacency_matrix[j][i] = -1

                num_edges += 1

    return adjacency_matrix, num_edges


# Adjustable
n_range = 15
edge_probability = 0.5
num_trials = 3

num_nodes = [i * 100 for i in range(1, n_range + 1)]
kahnam_time = []
kahnsl_time = []
tarjanam_time = []
tarjansl_time = []


# Test loop
for nodes in num_nodes:
    matrix, num_mtr_edges = rand_dag_adjacency(nodes, edge_probability)
    successor, num_suc_edges = rand_dag_successor(nodes, edge_probability)

    in_degree = [0] * nodes
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == -1:
                in_degree[i] += 1

    kahnam_time.append([])
    kahnsl_time.append([])
    tarjanam_time.append([])
    tarjansl_time.append([])

    for j in range(num_trials):
        # Kahn's algorithm with adjacency matrix
        k = KahnAm()
        k.am = copy.deepcopy(matrix)
        k.v = nodes
        k.e = num_mtr_edges

        k.in_degree = [0] * nodes
        k.not_visited = [True] * nodes

        start = time.perf_counter()
        k.start()
        kahnam_time[-1].append(time.perf_counter() - start)
        del k

        # Kahn's algorithm with successor list
        k = KahnSl()
        k.sl = copy.deepcopy(successor)
        k.v = nodes
        k.e = num_suc_edges

        k.in_degree = [0] * nodes
        k.not_visited = [True] * nodes

        start = time.perf_counter()
        k.start()
        kahnsl_time[-1].append(time.perf_counter() - start)
        del k

        # Tarjan's algorithm with adjacency matrix
        t = TarjanAm()
        t.am = copy.deepcopy(matrix)
        t.v = nodes
        t.e = num_mtr_edges

        t.not_visited = [True] * nodes

        start = time.perf_counter()
        t.start()
        ttt = time.perf_counter() - start
        tarjanam_time[-1].append(ttt)
        del t

        # Tarjan's algorithm with successor list
        t = TarjanSl()
        t.sl = copy.deepcopy(successor)
        t.v = nodes
        t.e = num_suc_edges

        t.not_visited = [True] * nodes

        start = time.perf_counter()
        t.start()
        tarjansl_time[-1].append(time.perf_counter() - start)
        del t


# Figure plotting
# Kahn's and Tarjan's algorithms comparison for adjacency matrix
plt.figure(figsize=(10, 6))
plt.plot(num_nodes, list(map(np.average, kahnam_time)), label='Kahn')
plt.errorbar(num_nodes, list(map(np.average, kahnam_time)), yerr=list(map(np.std, kahnam_time)),
             label='Kahn', fmt='none', ecolor='black', capsize=1)
plt.plot(num_nodes, list(map(np.average, tarjanam_time)), label='Tarjan')
plt.errorbar(num_nodes, list(map(np.average, tarjanam_time)), yerr=list(map(np.std, tarjanam_time)),
             label='Tarjan', fmt='none', ecolor='black', capsize=1)
plt.title('Comparison of Kahn\'s and Tarjan\'s algorithms for adjacency matrix')
plt.xlabel('Number of nodes (n)')
plt.ylabel('Time of function (s)')
plt.legend()
plt.savefig(f'figures/adjacency_matrix.png')
plt.show()

# Kahn's and Tarjan's algorithms comparison for successor list
plt.figure(figsize=(10, 6))
plt.plot(num_nodes, list(map(np.average, kahnsl_time)), label='Kahn')
plt.errorbar(num_nodes, list(map(np.average, kahnsl_time)), yerr=list(map(np.std, kahnsl_time)),
             label='Kahn', fmt='none', ecolor='black', capsize=1)
plt.plot(num_nodes, list(map(np.average, tarjansl_time)), label='Tarjan')
plt.errorbar(num_nodes, list(map(np.average, tarjansl_time)), yerr=list(map(np.std, tarjansl_time)),
             label='Tarjan', fmt='none', ecolor='black', capsize=1)
plt.title('Comparison of Kahn\'s and Tarjan\'s algorithms for successor list')
plt.xlabel('Number of nodes (n)')
plt.ylabel('Time of function (s)')
plt.legend()
plt.savefig(f'figures/successor_list.png')
plt.show()

# Kahn's algorithm comparison for adjacency matrix and successor list
plt.figure(figsize=(10, 6))
plt.plot(num_nodes, list(map(np.average, map(np.log10, kahnam_time))),
         label='Adjacency matrix')
plt.errorbar(num_nodes, list(map(np.average, map(np.log10, kahnam_time))),
             yerr=list(map(np.std, kahnam_time)), label='Adjacency matrix', fmt='none', ecolor='black', capsize=1)
plt.plot(num_nodes, list(map(np.average, map(np.log10, kahnsl_time))),
         label='Successor list')
plt.errorbar(num_nodes, list(map(np.average, map(np.log10, kahnsl_time))),
             yerr=list(map(np.std, kahnsl_time)), label='Successor list', fmt='none', ecolor='black', capsize=1)
plt.title('Comparison of adjacency matrix and successor list for Kahn\'s algorithm')
plt.xlabel('Number of nodes (n)')
plt.ylabel('Time of function (10^s)')
plt.legend()
plt.savefig(f'figures/kahn.png')
plt.show()

# Tarjan's algorithm comparison for adjacency matrix and successor list
plt.figure(figsize=(10, 6))
plt.plot(num_nodes, list(map(np.average, map(np.log10, tarjanam_time))),
         label='Adjacency matrix')
plt.errorbar(num_nodes, list(map(np.average, map(np.log10, tarjanam_time))),
             yerr=list(map(np.std, tarjanam_time)), label='Adjacency matrix', fmt='none', ecolor='black', capsize=1)
plt.plot(num_nodes, list(map(np.average, map(np.log10, tarjansl_time))),
         label='Successor list')
plt.errorbar(num_nodes, list(map(np.average, map(np.log10, tarjansl_time))),
             yerr=list(map(np.std, tarjansl_time)), label='Successor list', fmt='none', ecolor='black', capsize=1)
plt.title('Comparison of adjacency matrix and successor list for Tarjan\'s algorithm')
plt.xlabel('Number of nodes (n)')
plt.ylabel('Time of function (10^s)')
plt.legend()
plt.savefig(f'figures/tarjan.png')
plt.show()
