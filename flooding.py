from collections import deque

def flooding_search(graph, start_node, target_file, ttl, dead_nodes=None):
    if dead_nodes is None:
        dead_nodes = []

    if start_node in dead_nodes:
        return {
            "files_found": 0,
            "search_success": False,
            "messages_sent": 0,
            "nodes_reached": 0,
            "coverage_percent": 0,
            "duplicate_messages": 0
        }

    # Queue lưu cấu trúc: (current_node, current_ttl, parent_node)
    queue = deque()
    queue.append((start_node, ttl, None))

    # Từ điển lưu mức TTL lớn nhất mà một node từng nhận được
    visited_ttl = {}

    files_found = 0
    messages_sent = 0
    duplicate_messages = 0
    nodes_reached = set()

    while queue:
        current_node, current_ttl, parent_node = queue.popleft()

        if current_node in dead_nodes:
            continue

        # Nếu node đã xử lý gói tin này với TTL lớn hơn hoặc bằng 
        # -> Gói tin mới không tối ưu hơn, coi như là tin nhắn trùng lặp (Duplicate suppression)
        if current_node in visited_ttl and visited_ttl[current_node] >= current_ttl:
            duplicate_messages += 1
            continue

        # Ghi nhận/Cập nhật mức TTL tối ưu hơn cho node hiện tại
        visited_ttl[current_node] = current_ttl
        nodes_reached.add(current_node)

        # Kiểm tra sự tồn tại của File
        if target_file in graph.nodes[current_node]["files"]:
            files_found += 1

        # Nếu TTL đã cạn, không cho phép lan truyền tiếp
        if current_ttl <= 0:
            continue

        # Flood tin nhắn sang các node hàng xóm lân cận
        for neighbor in graph.neighbors(current_node):
            if neighbor in dead_nodes or neighbor == parent_node:
                continue

            messages_sent += 1
            queue.append((neighbor, current_ttl - 1, current_node))

    total_alive_nodes = len(graph.nodes()) - len(dead_nodes)
    coverage_percent = (
        (len(nodes_reached) / total_alive_nodes) * 100 
        if total_alive_nodes > 0 else 0
    )

    return {
        "files_found": files_found,
        "search_success": files_found > 0,
        "messages_sent": messages_sent,
        "duplicate_messages": duplicate_messages,
        "nodes_reached": len(nodes_reached),
        "coverage_percent": round(coverage_percent, 2)
    }