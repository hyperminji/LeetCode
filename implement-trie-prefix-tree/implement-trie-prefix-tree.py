class Trie:

    def __init__(self):
        self.root = {}
        self.end = '*'
        

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
                node = node[w]
            else:
                node = node[w]
        node[self.end] = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node:
                return False
            else:
                node = node[w]
        return self.end in node
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node :
                return False
            else:
                node = node[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)