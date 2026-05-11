class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for c in word:
                if c not in adj:
                    adj[c] = set()
        indegree = {c : 0 for c in adj}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        indegree[w2[j]] += 1
                        adj[w1[j]].add(w2[j])
                    break
        q = deque([c for c in indegree if indegree[c] == 0])
        ret = []
        while q:
            char = q.popleft()
            ret.append(char)
            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return "".join(ret) if len(ret) == len(adj) else ""