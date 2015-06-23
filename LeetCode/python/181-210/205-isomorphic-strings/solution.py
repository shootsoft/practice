class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        lst1 = list(s)
        lst2 = list(t)
        
        l1 = len(lst1)
        l2 = len(lst2)
        a = ord('a')
        if l1==l2:
            d = dict()
            k = dict()
            for i in range(l1):
                if lst1[i] not in d and lst2[i] not in k:
                    d[lst1[i]] = lst2[i]
                    k[lst2[i]] = lst1[i]
                elif lst1[i] in d and lst2[i] in k:
                    if d[lst1[i]] == lst2[i] and k[lst2[i]] == lst1[i]:
                        continue
                    else:
                        return False
                else:
                    return False
                
            
        else:
            return False
            
        return True