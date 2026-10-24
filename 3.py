from collections import deque

capacity = (4, 3)
start = (0, 0)
target = 2

queue = deque([(start, [])])
visited = {start}

while queue:
    (a, b), path = queue.popleft()

    if a == target or b == target:
        for step in path + [(a, b)]:
            print(step)
        break

    states = [
        (capacity[0], b),
        (a, capacity[1]),
        (0, b),
        (a, 0),
        (a - min(a, capacity[1] - b),
         b + min(a, capacity[1] - b)),
        (a + min(b, capacity[0] - a),
         b - min(b, capacity[0] - a))
    ]

    for state in states:
        if state not in visited:
            visited.add(state)
            queue.append((state, path + [(a, b)]))
else:
    print("No solution")
