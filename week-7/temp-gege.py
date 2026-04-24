from collections import deque
import sys


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    next_node = [x - 1 for x in data[1 : n + 1]]

    rev = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in enumerate(next_node):
        rev[v].append(u)
        indegree[v] += 1

    queue = deque(i for i in range(n) if indegree[i] == 0)
    in_cycle = [True] * n

    while queue:
        u = queue.popleft()
        in_cycle[u] = False
        v = next_node[u]
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)

    ans = [-1] * n
    seen_cycle = [False] * n

    for start in range(n):
        if not in_cycle[start] or seen_cycle[start]:
            continue

        cycle_nodes = []
        cur = start
        while not seen_cycle[cur]:
            seen_cycle[cur] = True
            cycle_nodes.append(cur)
            cur = next_node[cur]

        for c in cycle_nodes:
            ans[c] = c

        # Label every non-cycle predecessor tree with its entry cycle node.
        for c in cycle_nodes:
            stack = [c]
            while stack:
                node = stack.pop()
                for prev in rev[node]:
                    if in_cycle[prev] or ans[prev] != -1:
                        continue
                    ans[prev] = c
                    stack.append(prev)

    sys.stdout.write("\n".join(str(x + 1) for x in ans))


if __name__ == "__main__":
    solve()
