import networkx as nx
import random

NUM_NODES = 100
EDGE_PROBABILITY = 0.03
FILES_PER_NODE = 5
TOTAL_FILES = 200

FILE_POOL = [f"File_{i}" for i in range(TOTAL_FILES)]


def generate_network():
    """
    Sinh graph ngẫu nhiên liên thông gồm 100 node
    """

    while True:
        graph = nx.erdos_renyi_graph(
            n=NUM_NODES,
            p=EDGE_PROBABILITY
        )

        if nx.is_connected(graph):
            break

    for node in graph.nodes():
        graph.nodes[node]["files"] = random.sample(
            FILE_POOL,
            FILES_PER_NODE
        )

    return graph