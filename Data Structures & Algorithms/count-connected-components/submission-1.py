class Solution:
    def bfs(self,node, visit, adj):
        q = deque([node])
        visit[node] = True
        while q:
            cur = q.popleft()
            for nei in adj[cur]:
                if not visit[nei]:
                    visit[nei] = True
                    q.append(nei)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)



        res = 0
        for node in range(n):
            if not visit[node]:
                self.bfs(node, visit, adj)
                res += 1
        return res