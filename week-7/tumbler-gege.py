n = int(input())
P = list(map(int, input().split()))

for start in range(n):
    visited = set()
    current = start
    
    while True:
        if current in visited:
            print(current + 1)
            break
        
        visited.add(current)
        current = P[current] - 1