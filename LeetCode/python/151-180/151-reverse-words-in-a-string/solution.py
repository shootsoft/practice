class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):

        if s == None or s==[]:
            return s

        length = len(s)
        start = 0
        end = 0
        lst = list(s)


        for i in range(0, length):
            if lst[i]!=' ':
                end = i
                if i == length-1:
                    self.reverseArray(lst, start, end)

                #lst[i-offset] = lst[i]
                continue
            else:
                if start == i:
                    lst[i] = ''
                    start = i + 1
                else:
                    end = i - 1
                    self.reverseArray(lst, start, end)
                    start = i + 1


        end += 1
        if end < length and lst[end] == ' ':
            lst[end] =''

        # start = 0
        # for i in range(0, length):
        #     if lst[i]!=' ':
        #         continue
        #     else:
        #         end = i - 1
        #         self.reverseArray(lst, start, end)
        #         start = i + 1


        self.reverseArray(lst, 0, length-1)


        return ''.join(lst)

    def reverseArray(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def swap(self,nums, x, y):
        z = nums[x]
        nums[x] = nums[y]
        nums[y] = z
