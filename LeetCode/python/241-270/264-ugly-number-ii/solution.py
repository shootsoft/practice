class Solution:
    # @param {integer} num
    # @return {boolean}
    def nthUglyNumber2(self, n):

        total = 1
        base = [1]
        ha = set()
        ha.add(1)
        start = 0

        max = n * 5
        while total < max:

            end = len(base)
            last = base[end -1]
            for i in range(start, end):
                num = base[i] * 2
                if num not in ha:
                    base.append(num)
                    ha.add(num)
                    total += 1
                    if total == max:
                        break

                num = base[i] * 3
                if num not in ha:
                    base.append(num)
                    ha.add(num)
                    total += 1
                    if total == max:
                        break

                num = base[i] * 5
                if num not in ha:
                    base.append(num)
                    ha.add(num)
                    total += 1
                    if total == max:
                        break

            start = end

        base.sort()
        #print base
        return base[n-1]

    def nthUglyNumber(self, n):

        base = [1]
        i2 = i3 = i5 = 0
        while len(base) < n:

            n2, n3, n5 = base[i2] * 2,  base[i3] * 3,  base[i5] * 5,
            next = min(n2,n3,n5)
            if next == n2:
                i2 += 1
            if next == n3:
                i3 += 1
            if next == n5:
                i5 += 1
            base += next,
        #print base
        return base[n-1]