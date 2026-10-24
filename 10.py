import heapq

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1}
}

heuristic = {
    "A": 4,
    "B": 3,
    "C": 1,
    "D": 0
}

def astar(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            return path, g

        if g > best_cost.get(node, float("inf")):
            continue

        for neighbor, cost in graph[node].items():
            new_g = g + cost

            if new_g < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_g
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbor,
                     path + [neighbor])
                )

    return None, float("inf")

path, cost = astar("A", "D")

print("Best path:", path)
print("Total cost:", cost)
