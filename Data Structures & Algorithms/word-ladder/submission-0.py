class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        
        def matchWord(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
            
            return count

        
        adj = {}
        for s in wordList:
            adj[s] = []
        
        if beginWord not in adj:
            adj[beginWord] = []
        
        if endWord not in adj:
            adj[endWord] = []

        
        for s1 in adj.keys():
            for s2 in wordList:
                if matchWord(s1,s2) == 1:
                    adj[s1].append(s2)
        
        q = deque()
        q.append((beginWord, 1))

        myset = set()
        count = 0

        while q:
            word, steps = q.popleft()
            
            
            if word == endWord:
                return steps

            for s in adj[word]:
                if s not in myset:
                    q.append((s, steps+1));
                    myset.add(s)

        return 0


        
