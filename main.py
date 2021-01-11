# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import networkx
import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("In the first example we will get almost the same result, with 1 different edge, but with the same weight.\n")

    G = networkx.DiGraph()
    G = G.to_undirected()
    G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8])
    G.add_edge(0, 4, weight=2)
    G.add_edge(0, 6, weight=2)
    G.add_edge(1, 5, weight=2)
    G.add_edge(1, 7, weight=2)
    G.add_edge(2, 6, weight=2)
    G.add_edge(2, 8, weight=10)
    G.add_edge(3, 7, weight=2)

    # G.add_edge(0, 4, weight=1)
    # G.add_edge(0, 6, weight=3)
    # G.add_edge(1, 5, weight=1)
    # G.add_edge(1, 7, weight=3)
    # G.add_edge(2, 6, weight=1)
    # G.add_edge(2, 8, weight=10)
    # G.add_edge(3, 7, weight=1)

    answer = networkx.max_weight_matching(G)
    print("mine = ")
    print(answer)

    G2 = networkx.DiGraph()
    G2 = G2.to_undirected()
    G2.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8])
    G2.add_edge(0, 4, weight=1)
    G2.add_edge(0, 6, weight=1)
    G2.add_edge(1, 5, weight=1)
    G2.add_edge(1, 7, weight=1)
    G2.add_edge(2, 6, weight=1)
    G2.add_edge(2, 8, weight=1)
    G2.add_edge(3, 7, weight=1)

    answer2 = networkx.max_weight_matching(G2)
    print("class = ")
    print(answer2)

    print("\nIn the next example we will get the exact same result from both algos.\n")

    G3 = networkx.DiGraph()
    G3 = G3.to_undirected()
    G3.add_nodes_from([0, 1, 2, 3])
    G3.add_edge(0, 1, weight=2)
    G3.add_edge(0, 3, weight=3)
    G3.add_edge(1, 3, weight=3)
    G3.add_edge(2, 3, weight=4)

    answer3 = networkx.max_weight_matching(G3)
    print("mine = ")
    print(answer3)

    G4 = networkx.DiGraph()
    G4 = G4.to_undirected()
    G4.add_nodes_from([0, 1, 2, 3])
    G4.add_edge(0, 1, weight=1)
    G4.add_edge(0, 3, weight=1)
    G4.add_edge(1, 3, weight=1)
    G4.add_edge(2, 3, weight=1)

    answer4 = networkx.max_weight_matching(G4)
    print("class = ")
    print(answer4)

    print("\nIn the next example, we only have 2 options - 2 edges. One is worth 2, the other 13."
          "\nMy algo chooses the edge with higher weight, the algo from the class, when having only edges with weight=1, chooses the other one."
          "\nOf cousrse both still give the same amount of pairings.\n")

    G5 = networkx.DiGraph()
    G5 = G5.to_undirected()
    G5.add_nodes_from([0, 1, 2])
    G5.add_edge(0, 2, weight=2)
    G5.add_edge(1, 2, weight=13)

    answer5 = networkx.max_weight_matching(G5)
    print("mine = ")
    print(answer5)

    G6 = networkx.DiGraph()
    G6 = G6.to_undirected()
    G6.add_nodes_from([0, 1, 2])
    G6.add_edge(0, 2, weight=1)
    G6.add_edge(1, 2, weight=1)

    answer6 = networkx.max_weight_matching(G6)
    print("class = ")
    print(answer6)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
