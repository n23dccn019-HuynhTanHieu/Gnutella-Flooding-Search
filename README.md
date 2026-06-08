# Gnutella Flooding Search Simulation

## Author

**Huỳnh Tấn Hiếu**
**Student ID:** N23DCCN019

**Course:** Distributed Database Systems

**Project Topic 62:** Gnutella-Style Flooding: Unstructured Search

---

## Project Overview

This project implements a simplified Gnutella-style Flooding Search algorithm on an unstructured Peer-to-Peer (P2P) network.

The simulation evaluates how different Time-To-Live (TTL) values affect:

* Search Coverage
* Network Overhead
* Search Success Rate

The project also analyzes the impact of node failures by simulating the failure of the highest-degree hub node.

---

## Theoretical Background

This project is based on the concepts of unstructured Peer-to-Peer (P2P) systems presented by Özsu and Valduriez in distributed database systems.

In an unstructured P2P network, peers do not maintain a global index of resources. Resource discovery is typically performed using query flooding. While flooding can achieve high search coverage, it may also generate a large number of messages, creating significant communication overhead.

This simulation demonstrates the trade-off between search effectiveness and network cost by evaluating different TTL values and analyzing the impact of hub node failures.

---

## Network Configuration

| Parameter           | Value                    |
| ------------------- | ------------------------ |
| Number of Nodes     | 100                      |
| Graph Model         | Erdős–Rényi Random Graph |
| Edge Probability    | 0.03                     |
| Files per Node      | 5                        |
| Total File Pool     | 200                      |
| TTL Values Tested   | 3, 5, 7                  |
| Experiments per TTL | 50                       |

---

## Features

* Random P2P network generation
* Flooding-based search algorithm
* Time-To-Live (TTL) control
* Search coverage measurement
* Network overhead measurement
* Duplicate message tracking
* Success rate analysis
* Hub node failure simulation
* Automatic graph generation

---

## Project Structure

```text
GnutellaFlooding/
│
├── main.py
├── graph_generator.py
├── flooding.py
├── analysis.py
├── failure_analysis.py
│
├── benchmark_results.csv
├── network_topology.png
├── coverage_vs_overhead.png
├── coverage_by_ttl.png
└── failure_analysis.png
```

---

## Requirements

Install required packages:

```bash
pip install networkx pandas matplotlib
```

---

## Running the Project

Execute:

```bash
python main.py
```

---

## Example Console Output

```text
============================================================
GNUTELLA FLOODING SEARCH SIMULATION
============================================================

[INFO] Network Nodes : 100
[INFO] Network Edges : 150

[INFO] Start Node : 47
[INFO] Highest Degree Hub Node : 18

Running Benchmark Analysis...
Running Failure Analysis...

All tasks completed successfully.
```

---

## Generated Outputs

### 1. Network Topology

Visual representation of the generated P2P network.

Output:

```text
network_topology.png
```

### 2. Benchmark Results

Average metrics for TTL values 3, 5, and 7.

Output:

```text
benchmark_results.csv
```

Metrics:

* Coverage (%)
* Average Messages Sent
* Duplicate Messages
* Average Files Found
* Success Rate (%)

### 3. Search Coverage vs Network Overhead

Shows the relationship between:

* Average Messages Sent
* Average Files Found

Output:

```text
coverage_vs_overhead.png
```

### 4. Coverage by TTL

Shows how increasing TTL affects network coverage.

Output:

```text
coverage_by_ttl.png
```

### 5. Hub Failure Analysis

Compares search coverage between:

* Normal Network
* Hub Node Failure

Output:

```text
failure_analysis.png
```

---

## Experimental Results

Typical observations:

* TTL = 3 produces low overhead but limited coverage.
* TTL = 5 significantly improves coverage.
* TTL = 7 reaches nearly full coverage but introduces substantial network overhead.
* Hub node failures reduce search efficiency and overall coverage.

These results demonstrate the classic flooding trade-off between search effectiveness and communication cost in unstructured P2P networks.

---

## References

1. Özsu, M. T., & Valduriez, P. *Principles of Distributed Database Systems*, Third Edition, Springer, 2011.

2. Gnutella Protocol Development Documentation.

---

## Conclusion

This project successfully simulates Gnutella-style Flooding Search in an unstructured P2P network. The results show that increasing TTL improves search coverage and file discovery but also increases communication overhead. The hub failure experiment further demonstrates the importance of highly connected nodes in maintaining network efficiency.
