class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(cur, word):
            if len(word) == 0 :
                if cur.endOfWord:
                    return True
                return False
            

            if word[0] == '.':
                for ch in cur.children.keys():
                    if(dfs(cur.children[ch], word[1:])):
                        return True
            elif word[0] in cur.children:
                return dfs(cur.children[word[0]], word[1:])

            return False
        
        return dfs(cur, word)
            

                
