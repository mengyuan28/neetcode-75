class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        head = self.root
        for c in word:
            i = ord(c) - ord('a')
            if head.children[i] == None:
                head.children[i] = TrieNode()
            head = head.children[i]
        head.isEnd = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children:
                        if child is not None:
                            if dfs(i+1, child):
                                return True
                    return False
                else:
                    index = ord(c) - ord('a')
                    if cur.children[index] is None:
                        return False
                    cur = cur.children[index]
            return cur.isEnd
        return dfs(0, self.root)
        
