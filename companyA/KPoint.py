__author__ = 'yinjun'


'''
Point object
'''
class Point:

    ###
    # Init object
    ###
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = None

    '''
    Obtain approximate distance
    '''
    def getDistance(self):
        if self.distance == None:
            self.distance = self.assumeSqrt(self.x * self.x + self.y * self.y)
        return self.distance

    '''
    Obtain approximate sqrt
    '''
    def assumeSqrt(self, n):
        start = 0
        end = n
        s = 0
        while start + 1 < end:
            m = (start + end) / 2
            s = m * m

            if s > n:
                end = m
            elif s < n:
                start = m
            else:
                start = m
                break

        return start
        # end of assumeSqrt

    ###
    # for better print
    ###
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    ###
    # for better list print
    ###
    def __repr__(self):
        return str(self)

'''
Get closest K points to origin from N points stream
'''
class KPoint:

    ###
    # Init KPoint with memory size
    ###
    def __init__(self, memorySize):
        self.memorySize = memorySize
        self.__init_queue__()
        self.__init_disk__()

    ###
    # Init memory queue
    ###
    def __init_queue__(self):
        #in memory queue
        self.queue = []

    ###
    # Init disk simulation
    ###
    def __init_disk__(self):
        self.disk = []

    '''
    Get K closest points to the origin
    @:param points stream point list [[0,0],[1,1],[2,2]...]
    @:param K quality to obtain in stream
    '''
    def getKpoints(self, points, K):
        if K > self.memorySize:
            return self.inDiskFile(points, K)
        else:
            return self.inMemoryList(points, K)
        #end of getPoints

    '''
    Get K points to the origin in memory
    '''
    def inMemoryList(self, points, K):
        self.__init_queue__()
        for po in points:
            p = Point(po[0], po[1])
            self.__insert__(self.queue, p)
            if len(self.queue) > K:
                self.__drop_last__()
        return self.queue
        #end of inMemoryList


    ###
    # insert an element into the memory queue
    ###
    def __insert__(self, queue, point):
        # TODO: Use binary search to get higher performance
        length = len(queue)
        if length == 0:
            queue.append(point)
        else:
            isBreak = False
            for i in range(length):
                if point.getDistance() < queue[i].getDistance():
                    queue.insert(i, point)
                    isBreak = True
                    break
            if not isBreak:
                queue.append(point)
        # end of __insert

    ###
    # drop the last element of the queue
    ###
    def __drop_last__(self):
        if len(self.queue)>0:
            self.queue.pop()
        #end of __drop_last__


    '''
    Get K points to the origin from disk file
    '''
    def inDiskFile(self, points, K):

        self.__init_disk__()
        # Temp queue
        queue = []
        length = 0

        for po in points:
            p = Point(po[0], po[1])
            if length < self.memorySize:
                self.__insert__(queue, p)
                length += 1
            else:
                self.disk.append(queue)
                queue = []
                length = 0

        #store the last group of list
        if length>0:
            self.disk.append(queue)
            queue = []
            length = 0

        return self.__grab_from_disk__(K)


    ###
    # grab K points from disk
    ###
    def __grab_from_disk__(self, K):

        # TODO: Optimize the disk file, maybe merge disk file first then grab, like (((file1) (file2)) ((file3)(file4)))
        # TODO: After merging, will get higher performance
        streamReturn = []
        while K > 0:
            sub = self.__grab_from_disk_sub__(K)
            length = len(sub)
            K -= length
            streamReturn += sub
        return streamReturn

    ###
    # grab K points from disk, but due to the limitation of memory, every time return max length == memorySize
    ###
    def __grab_from_disk_sub__(self, K):

        # TODO: Optimize the read sequence, because every time, when dumping queue into a new file, the file contains second closest to origin
        # temp queue for grab
        queue = []
        length = 0
        remove = []
        for i in range(len(self.disk)):
            if length < self.memorySize:
                if len(self.disk[i]) > 0:
                    p = self.disk[i].pop(0)
                    self.__insert__(queue, p)
                else:
                    remove.append(i - len(remove))
            else:
                # sotre half of temp queue in to new disk
                length  = length/2
                self.disk.append(queue[length:])
                queue = queue[0:length]

        #delete empty file
        while len(remove) > 0:
            i = remove.pop(0)
            self.disk.pop(i)

        if length>K:
            return queue[0:K]
        else:
            return queue