t = int(input())

for _ in range(t):
    n, m, s = map(int, input().split())
    
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    dist = [-1] * (n + 1)
    dist[s] = 0
    
    queue = [s]
    front = 0
    while front < len(queue):
        node = queue[front]
        front += 1
        
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    max_dist = -1
    farthest_node = n + 1
    
    for i in range(1, n + 1):
        if dist[i] > max_dist:
            max_dist = dist[i]
            farthest_node = i
        elif dist[i] == max_dist and i < farthest_node:
            farthest_node = i
    
    print(farthest_node, max_dist)