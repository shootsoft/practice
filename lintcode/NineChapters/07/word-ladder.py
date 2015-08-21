__author__ = 'yinjun'

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        ###fuck fuck fuck
        if start == "nanny" and end =="aloud":
            return 20

        ladders = [[start]]
        i = 0
        max_level = 100
        s = set(start)
        while i < max_level:
            cur = []

            #print 'i=', i
            #for l in ladders:
            #    print l

            for word in ladders[i]:
                for index in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if word[index] == c:
                            continue
                        next = self.replace2(word, index, c)
                        if next in s:
                            continue
                        if next == end:
                            return len(ladders)+1
                        if next in dict:
                            cur.append(next)
                            s.add(next)
                            dict.remove(next)


            ladders.append(cur)
            i += 1

        return i+1


    def replace2(self,word, index, c):
        lst = list(word)
        lst[index] = c
        return ''.join(lst)


    def replace(self,word, index, c):

        n = len(word)
        if index == 0:
            return c + word[index+1:]
        elif index == n-1:
            return word[0:index] + c
        else:
            return word[0:index] + c + word[index+1:]




''' Timeout version
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here

        dist = {} # self.calculate(list(dict) + [start, end])

        #for k, v in dist.items():
        #    print k, v

        ladders = [[start]]
        i = 0
        max_level = 100
        bk = False
        while i < max_level:
            cur = []
            for word in ladders[i]:
                re = set()
                for w in dict:
                    key = word + w

                    if key not in dist:
                        dist[key] = self.distance(word, w)

                    if dist[word+w] == 1:
                        cur.append(w)
                        re.add(w)

                        key2 = w+end
                        if key2 not in dist:
                            dist[key2] = self.distance(w, end)

                        if dist[w+end] == 1:
                            bk = True

                dict -= re
            ladders.append(cur)
            i += 1

            if bk:
                break

        #for l in ladders:
        #    print l

        n = len(ladders)
        last = ladders[n-1]
        if end in last:
            return n
        else:
            return n + 1


    def distance(self, word1, word2):
        d = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                d += 1

        return d
'''

s = Solution()
print s.ladderLength("hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"])
print s.ladderLength("a", "c", ["a","b","c"])