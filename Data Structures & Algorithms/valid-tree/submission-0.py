class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        v = len(edges)
        # 1 - 2
        if v > n-1:
            return False
        adj = [[] for _ in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        q = deque() # current node, parent node
        q.append((0,-1))
        visit.add(0)
        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                q.append((nei, node))
                visit.add(nei)
        
        return len(visit) == n

        
