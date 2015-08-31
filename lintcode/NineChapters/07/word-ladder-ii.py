class Node:
    def __init__(self, word, path=[]):
        self.word = word
        self.next = []
        self.path = path + [word]


class Solution:

    def __init__(self):
        self.cache = {}
        self.dict = {}

    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        cur = Node(start)
        #print cur.path
        results = cur
        queue = [cur]
        final = []
        pos = 0
        self.dict = dict
        isRunning = True
        if start in dict:
            dict.remove(start)

        d = self.distance(start, end)
        if d<=1:
            eNode = Node(end, cur.path)
            final.append(eNode.path)
            results.next.append(eNode)
        else:
            if end in dict:
                dict.remove(end)

            #print start, end,  dict
            while isRunning:

                next_pos = len(queue)
                for i in range(pos, len(queue)):
                    # if word == end:
                    #     isRunning = False
                    #     match.add(word)
                    wnode = queue[i]

                    d = self.distance(wnode.word, end)
                    if d<=1:
                        eNode = Node(end, wnode.path)

                        final.append(eNode.path)
                        results.next.append(eNode)
                        isRunning = False
                    else:

                        nexts = self.find_next(wnode.word)
                        for w in nexts:
                            nNode = Node(w, wnode.path)
                            #print 'mb', nNode.path
                            queue.append(nNode)
                            wnode.next.append(nNode)
                        #
                        # for j in range(len(wnode.word)):
                        #     nexts = self.find()
                        #
                        # match = set()
                        # for next in dict:
                        #     d = self.distance(wnode.word, next)
                        #     if d>1:
                        #         continue
                        #     else:
                        #         match.add(next)
                        #         nNode = Node(next, wnode.path)
                        #         #print 'mb', nNode.path
                        #         queue.append(nNode)
                        #         wnode.next.append(nNode)
                        # #print 'remove', match
                        # #dict -= match
                pos = next_pos

            #print results

        return final


    def distance(self, word1, word2):
        #print word1, word2
        key = word1 + word2
        if key in self.cache:
            return self.cache[key]
        else:
            if word1 == word2:
                self.cache[key] = 0
                return 0
            else:
                r = 0
                for i in range(len(word1)):
                    if word1[i] != word2[i]:
                        r += 1
                self.cache[key] = r
                return r

    def find_next(self, word):
        nexts = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                w = self.replace(word, i , c)
                if w in self.dict:
                    nexts.append(w)
        return nexts

    def replace(self, word, index, c):
        n = len(word)
        if index == 0:
            return c + word[index+1:]
        elif index == n-1:
            return word[0:index] + c
        else:
            return word[0:index] + c + word[index+1:]

s = Solution()
#print s.findLadders("a", "c", set(["a","b","c"]))
#print s.findLadders("hit", "cog", set(["hot","dot","dog","lot","log"]))
#print s.findLadders("hot", "dog", set(["hot","cog","dog","tot","hog","hop","pot","dot"]))
print s.findLadders("teach", "place", set(["peale","wilts","place","fetch","purer","pooch","peace","poach","berra","teach","rheum","peach"]))

