from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph: dict[int, list[int]] = build_graph(isConnected)
        answer, total_visited = 0, set()
        for key, value in graph.items():
            if key not in total_visited:
                total_visited |= dfs(key, graph)
                answer += 1
        return answer

def build_graph(isConnected: list[list[int]]) -> dict[int, list[int]]:
    graph = defaultdict(list)
    for i in range(len(isConnected)):
        for j in range(len(isConnected[0])):
            if isConnected[i][j]: graph[i].append(j)
    return graph

def dfs(node, graph) -> set[int]:
    visited = set()
    stack = [node]
    while stack:
        node = stack.pop()
        if node not in visited:
            stack.extend(graph[node])
            visited.add(node)
    return visited
