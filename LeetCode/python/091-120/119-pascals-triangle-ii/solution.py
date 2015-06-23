class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def getRow(self, numRows):
       return self.generateResult(numRows+1)
    
    def generateResult(self, numRows):
        
        if numRows == 0:
            return []
            
        if numRows == 1:
            return [1]
        elif numRows == 2:
            return [1,1]
        else:
            result = self.generateResult(numRows-1)
            cur = [result[0]]
            for i in range(1, len(result)):
                cur.append( result[i-1] + result[i])
            cur.append(result[numRows-2])
            return cur
            
            