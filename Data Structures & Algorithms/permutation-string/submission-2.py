class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        left = 0
        check = defaultdict(int)
        for i in range(len(s2)):
            cur = s2[i]
            if cur not in counter:
                check = defaultdict(int)
                left = i
                continue
            check[cur] += 1
            while left < len(s2) and check[cur] > counter[cur]:
                check[s2[left]] -= 1
                left +=1 
            if check == counter:
                return True
        return False
