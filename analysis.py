import random
import pandas as pd
import matplotlib.pyplot as plt

from graph_generator import generate_network
from flooding import flooding_search


def run_analysis():
    ttl_values = [3, 5, 7]
    NUM_EXPERIMENTS = 50
    results = []

    # FIX: Tạo sẵn 50 kịch bản test case (Đồ thị cố định, node bắt đầu, mục tiêu tìm kiếm)
    test_cases = []
    for _ in range(NUM_EXPERIMENTS):
        graph = generate_network()
        start_node = random.choice(list(graph.nodes()))
        random_node = random.choice(list(graph.nodes()))
        target_file = random.choice(graph.nodes[random_node]["files"])
        test_cases.append((graph, start_node, target_file))

    # Chạy thực nghiệm đồng bộ
    for ttl in ttl_values:
        total_messages = 0
        total_duplicates = 0
        total_coverage = 0
        total_files_found = 0
        total_success = 0

        for graph, start_node, target_file in test_cases:
            result = flooding_search(
                graph=graph,
                start_node=start_node,
                target_file=target_file,
                ttl=ttl
            )

            total_messages += result["messages_sent"]
            total_duplicates += result["duplicate_messages"]
            total_coverage += result["coverage_percent"]
            total_files_found += result["files_found"]

            if result["search_success"]:
                total_success += 1

        results.append({
            "TTL": ttl,
            "Coverage %": round(total_coverage / NUM_EXPERIMENTS, 2),
            "Avg Messages": round(total_messages / NUM_EXPERIMENTS, 2),
            "Duplicate Msgs": round(total_duplicates / NUM_EXPERIMENTS, 2),
            "Avg Files Found": round(total_files_found / NUM_EXPERIMENTS, 2),
            "Success Rate %": round(total_success / NUM_EXPERIMENTS * 100, 2)
        })

    df = pd.DataFrame(results)

    print("\n========== BENCHMARK RESULTS ==========\n")
    print(df)

    df.to_csv("benchmark_results.csv", index=False)
    create_graphs(df)
    return df


def create_graphs(df):
    # Graph 1: Files Found vs Messages Sent
    plt.figure(figsize=(8, 6))
    plt.plot(df["Avg Messages"], df["Avg Files Found"], marker="o", linewidth=2, color="dodgerblue")
    
    for _, row in df.iterrows():
        plt.annotate(
            f"TTL={int(row['TTL'])}",
            (row["Avg Messages"], row["Avg Files Found"]),
            textcoords="offset points",
            xytext=(0,10),
            ha='center'
        )

    plt.xlabel("Average Messages Sent (Network Overhead)")
    plt.ylabel("Average Files Found")
    plt.title("Files Found vs Network Overhead")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig("coverage_vs_overhead.png", dpi=300, bbox_inches="tight")
    print("[INFO] Saved: coverage_vs_overhead.png")
    plt.close()

    # Graph 2: Coverage vs TTL
    plt.figure(figsize=(8, 6))
    plt.bar(df["TTL"].astype(str), df["Coverage %"], color="skyblue", edgecolor="gray")
    plt.xlabel("TTL (Time-to-Live)")
    plt.ylabel("Coverage (%)")
    plt.title("Network Coverage for Different TTL Values")
    plt.ylim(0, 105)
    plt.savefig("coverage_by_ttl.png", dpi=300, bbox_inches="tight")
    print("[INFO] Saved: coverage_by_ttl.png")
    plt.close()