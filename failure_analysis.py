import random
import matplotlib.pyplot as plt

from graph_generator import generate_network
from flooding import flooding_search


def run_failure_analysis():
    graph = generate_network()

    # Lấy Hub Node có degree lớn nhất trong đồ thị
    hub_node = max(graph.degree, key=lambda x: x[1])[0]

    # FIX: Chọn ngẫu nhiên một start_node nằm ngoài Hub Node để tránh lỗi cô lập ngay từ đầu
    available_nodes = [node for node in graph.nodes() if node != hub_node]
    start_node = random.choice(available_nodes)

    # Lấy ngẫu nhiên file đích cần tìm kiếm trong mạng
    target_node = random.choice(list(graph.nodes()))
    target_file = random.choice(graph.nodes[target_node]["files"])

    # Giả lập 2 kịch bản mạng bình thường và mạng mất Hub
    normal_result = flooding_search(
        graph,
        start_node,
        target_file,
        ttl=5
    )

    failed_result = flooding_search(
        graph,
        start_node,
        target_file,
        ttl=5,
        dead_nodes=[hub_node]
    )

    labels = ["Normal Network", "Hub Node Failed"]
    coverage = [
        normal_result["coverage_percent"],
        failed_result["coverage_percent"]
    ]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, coverage, color=['skyblue', 'lightcoral'], edgecolor="gray")
    plt.ylabel("Coverage (%)")
    plt.title(f"Effect of Hub Failure (Node {hub_node})")
    plt.ylim(0, 105)

    plt.savefig("failure_analysis.png", dpi=300, bbox_inches="tight")
    print(f"[INFO] Hub Node Failed: {hub_node}")
    print("[INFO] Saved: failure_analysis.png")
    plt.close()