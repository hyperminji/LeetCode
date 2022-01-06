class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, word, index):
        cur_node = self.root
        
        if self.is_pal(word):
            if 'pal' not in cur_node: cur_node['pal'] = []
            cur_node['pal'] += [index]
        
        for i,c in enumerate(word):
            if c not in cur_node:
                cur_node[c] = {}
            cur_node= cur_node[c]
                
            if self.is_pal(word[i+1:]):
                if 'pal' not in cur_node: cur_node['pal'] = []
                cur_node['pal'] += [index]
                
        
        cur_node['end'] = index
        
    def get(self): return self.root
    
    def is_pal(self, word): return word==word[::-1]
    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        trie = Trie()
        empty_word_present = False 
        
        for i, word in enumerate(words):
            trie.insert(word[::-1], i)
            
        
        #now check for pairs
        ans =set()

        for index, word in enumerate(words):
            n = len(word)
            cur_node = trie.get()
            
            #handle empty words
            if 'end' in cur_node and trie.is_pal(word):
                if cur_node['end']!= index: ans.add((index, cur_node['end']))
                   
            
            word_traversal_complete= True
            for i in range(n):
                c = word[i]
            
                if c in cur_node:
                    cur_node =cur_node[c]
                    
                else:
                    #if there is no corresponfing word break, 
                    #then we could skip word altogether
                    word_traversal_complete = False
                    break
                    
                #left is large and right is short (ends early)
                if 'end' in cur_node and trie.is_pal(word[i+1:]):
                    if cur_node['end']!= index: ans.add((index, cur_node['end']))
            
            #left is small and right has more string, which could be a palindrome
            if word_traversal_complete and 'pal' in cur_node: 
                for j in cur_node['pal']:
                    if j!= index: ans.add((index, j))
                
        return ans

'''
# 트라이 저장할 노드
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    # 단어 삽입
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            #두번째 로직에서 문자를 제거해가면서 팰린드롬 판별 체크
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            # 판별 로직 3) 탐색 중간에 word_id가 있고 나머지 문자가 펠린드롬
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 판별 로직 1) 끝까지 탐색했을 때 word_id가 있는 경우
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별 로직 2) 끝까지 탐색했을 때 palindrome_word_ids가 있고 나머지 팰린드롬
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results
'''