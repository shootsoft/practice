class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):

        length = len(num)
        if length < 2 :
            return

        for i in range(length - 2, -1, -1):
            if num[i] < num[i+1]:
                break

        for k in range(length -1, i-1, -1):
            if num[i] < num[k]:
                break

        if i>=0 :
            m = num[i]
            num[i] = num[k]
            num[k] = m

    self.r
        num.reverse()



     if (num.size() < 2) return;
 5         int i, k;
 6         for (i = num.size() - 2; i >= 0; --i) if (num[i] < num[i+1]) break;
 7         for (k = num.size() - 1; k > i; --k) if (num[i] < num[k]) break;
 8         if (i >= 0) swap(num[i], num[k]);
 9         reverse(num.begin() + i + 1, num.end());