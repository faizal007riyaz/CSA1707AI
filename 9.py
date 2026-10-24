from itertools import permutations

cities = ["A", "B", "C", "D"]

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_cost = float("inf")
best_route = None

for route in permutations(range(1, len(cities))):
    path = (0,) + route + (0,)

    cost = sum(
        dist[path[i]][path[i+1]]
        for i in range(len(path)-1)
    )

    if cost < best_cost:
        best_cost = cost
        best_route = path

print("Best route:",
      " -> ".join(cities[i] for i in best_route))
print("Minimum cost:", best_cost)
