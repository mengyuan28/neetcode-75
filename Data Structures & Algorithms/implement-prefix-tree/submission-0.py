class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i]:
                cur = cur.children[i]
            else:
                cur.children[i] = TrieNode()
                cur = cur.children[i]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i]:
                cur = cur.children[i]
            else:
                return False
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if cur.children[i]:
                cur = cur.children[i]
            else:
                return False
        return True
        
        