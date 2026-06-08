import random
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D

from graph_generator import generate_network
from analysis import run_analysis
from failure_analysis import run_failure_analysis


def visualize_network(graph, dead_node=None, start_node=0):
    """
    Visualize Gnutella network topology
    """

    plt.figure(figsize=(10, 10))

    pos = nx.spring_layout(
        graph,
        seed=42
    )

    node_colors = []

    for node in graph.nodes():

        if node == dead_node:
            node_colors.append("red")

        elif node == start_node:
            node_colors.append("lime")

        else:
            node_colors.append("skyblue")

    nx.draw_networkx_nodes(
        graph,
        pos,
        node_size=100,
        node_color=node_colors
    )

    nx.draw_networkx_edges(
        graph,
        pos,
        alpha=0.25,
        edge_color="gray"
    )

    legend_elements = [

        Line2D(
            [0],
            [0],
            marker='o',
            color='w',
            label='Normal Node (Peer)',
            markerfacecolor='skyblue',
            markersize=8
        ),

        Line2D(
            [0],
            [0],
            marker='o',
            color='w',
            label='Source Node (Query Origin)',
            markerfacecolor='lime',
            markersize=8
        ),

        Line2D(
            [0],
            [0],
            marker='o',
            color='w',
            label='Failed Hub Node',
            markerfacecolor='red',
            markersize=8
        )
    ]

    plt.legend(
        handles=legend_elements,
        loc="upper right"
    )

    plt.title(
        f"Gnutella Network Topology\n"
        f"Source Node = {start_node} | Failed Hub = {dead_node}"
    )

    plt.axis("off")

    plt.savefig(
        "network_topology.png",
        dpi=300,
        bbox_inches="tight"
    )

    print(
        "[INFO] Saved: network_topology.png"
    )

    plt.close()


def main():

    print("=" * 60)
    print("GNUTELLA FLOODING SEARCH SIMULATION")
    print("=" * 60)

    print("\nGenerating network...")

    graph = generate_network()

    # Tìm hub node có degree lớn nhất
    hub_node = max(
        graph.degree,
        key=lambda x: x[1]
    )[0]

    # Chọn source node khác hub node
    available_nodes = [
        node
        for node in graph.nodes()
        if node != hub_node
    ]

    start_node = random.choice(
        available_nodes
    )

    print(
        f"[INFO] Network Nodes : {graph.number_of_nodes()}"
    )

    print(
        f"[INFO] Network Edges : {graph.number_of_edges()}"
    )

    print(
        f"[INFO] Start Node : {start_node}"
    )

    print(
        f"[INFO] Highest Degree Hub Node : {hub_node}"
    )

    visualize_network(
        graph,
        dead_node=hub_node,
        start_node=start_node
    )

    print("\nRunning Benchmark Analysis...")
    run_analysis()

    print("\nRunning Failure Analysis...")
    run_failure_analysis()

    print("\nAll tasks completed successfully.")

    print("\nGenerated Files:")
    print("- network_topology.png")
    print("- benchmark_results.csv")
    print("- coverage_vs_overhead.png")
    print("- coverage_by_ttl.png")
    print("- failure_analysis.png")


if __name__ == "__main__":
    main()