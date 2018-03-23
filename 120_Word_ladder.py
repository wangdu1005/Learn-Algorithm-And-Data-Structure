__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["jiuzhang, Wangdu Lin"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wangdu Lin"
__email__ = "wangdu1005@gmail.com"
__status__ = "Production"

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # Avoid modify input data.
        wordSet = set([])
        for word in dict:
            wordSet.add(word)
        wordSet.add(end)
        print(wordSet)
        
        wordLen = len(start)
        q = collections.deque([(start, 1)])
        while q:
            currWord, currLen = q.popleft()
            if currWord == end:
                return currLen
            else:
                # In this double for loop, the first for loop is to looping every position of word.
                for i in range(wordLen):
                    part1, part2 = currWord[:i], currWord[i+1:]
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        # Ignore the same letter in current word i position, becasue at start of init the deque,
                        # we already check the start word in the first while loop. 
                        # And others nextWord will also be check in the beginning of while loop first "if statement".
                        # Therefore, we only check those different from currWord's letter.
                        if currWord[i] != j:
                            nextWord = part1 + j + part2
                            if nextWord in wordSet:
                                q.append((nextWord, currLen + 1))
                                wordSet.remove(nextWord)
        return 0