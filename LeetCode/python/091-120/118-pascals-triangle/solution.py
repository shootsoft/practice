class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
       result = []
       self.generateResult(numRows, result)
       return result
    
    def generateResult(self, numRows, result):
        
        if numRows == 0:
            return
            
        if numRows == 1:
            result.append([1])
        elif numRows == 2:
            self.generateResult(numRows-1, result)
            result.append([1,1])
        else:
            self.generateResult(numRows-1, result)
            #print result
            last = result[numRows-2]
            cur = [last[0]]

            for i in range(1, len(last)):
                cur.append( last[i-1] + last[i])
            cur.append(last[numRows-2])
            result.append(cur)
            
            