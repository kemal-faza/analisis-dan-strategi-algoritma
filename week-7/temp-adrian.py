import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    s = next(it)

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a = next(it)
        b = next(it)
        graph[a].append(b)

    def dfs(node: int, visited: set[int]) -> bool:
        if node == s:
            return True

        visited.add(node)
        for nxt in graph[node]:
            if nxt == s:
                return True
            if nxt not in visited and dfs(nxt, visited):
                return True
        return False

    can_return = False
    for neighbor in graph[s]:
        if dfs(neighbor, {s}):
            can_return = True
            break

    print("YES" if can_return else "NO")


if __name__ == "__main__":
    main()
