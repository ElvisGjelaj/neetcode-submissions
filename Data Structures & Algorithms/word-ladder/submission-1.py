class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        queue = deque([beginWord])
        steps = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return steps

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nxt = word[:i] + c + word[i + 1:]
                        if nxt in words:
                            words.remove(nxt)
                            queue.append(nxt)
            steps += 1
        
        return 0