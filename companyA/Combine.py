__author__ = 'yinjun'

'''
Calcuate combinations
'''
class Combine:

    ###
    # init result set
    ###
    def __init__result__(self):
        self.results = []

    '''
    Calculate combinations (of any length) that add up to that target_sum
    @:param nums integer array
    @:param target integer
    '''
    def calculate_combinations(self, nums, target_sum):
        # init result
        self.__init__result__()

        if nums != None and nums != [] and target_sum != None:
            self.__calculate_combinations_help__(nums, target_sum, 0, [])
        return self.results

    def __calculate_combinations_help__(self, nums, target, start, result):

        if target == 0 and len(result) > 0:
            self.results.append(result[:])
        for i in range(start, len(nums)):
            result.append(nums[i])
            self.__calculate_combinations_help__(nums, target - nums[i], i + 1, result)
            result.pop()


