'''
Interviewee: Wangdu Lin
Email: wangdu1005@gmail.com
Test Date Time: 2018/03/26 10:00:00 AM
Programming Lauange: Python 2.7.10
Time complexity: O(m * n)
Space complexity: O(n)
'''

class Solution:

    '''
    Idea of solution:
    I tried varies solutions, but in the end I choosed in-by-min search to be my release solution.
    The main ideas is to scan every mins between earliest start time and latest end time of all reservations. 
    Then I can know how many reserved tables on that specific min. 
    Finally I can found out the minimize table amount by compare every table's demand on each mins.
    '''
    def calculateMinTable(self, schedule):
        if schedule is None:
            return None

        # Time: O(1)
        def timeToNumber(timeRange):
            start = int(timeRange[0][:2]) * 60 + int(timeRange[0][3:])
            end = int(timeRange[1][:2]) * 60 + int(timeRange[1][3:])
            return (start, end)

        # map() ---> Time: O(n)
        timeRangeData = list(map(timeToNumber, schedule))
        print('Time Range Data: ' + str(timeRangeData))

        # Find the earliest start time ---> Time: O(n)
        minStartTime = float('inf')
        for start, _ in timeRangeData:
            if start < minStartTime:
                minStartTime = start

        print('minStartTime: ' + str(minStartTime))

        # Find the latest end time ---> Time: O(n)
        maxEndTime = float('-inf')
        for _, end in timeRangeData:
            if end > maxEndTime:
                maxEndTime = end
        print('maxEndTime: ' + str(maxEndTime))
        from collections import defaultdict
        dataDict = defaultdict(list)

        # in-by-min search
        # double for loop ---> O(m * n) 
        for mins in range(minStartTime, maxEndTime + 1):
            # print(mins)
            countTable = 0
            for start, end in timeRangeData:
                if mins >= start and mins <= end:
                    countTable += 1
                    dataDict[mins] = countTable
        
        leastRequireTable = float('-inf')
        # for loop ---> Time: O(n)
        for key, count in dataDict.items():
            if count > leastRequireTable:
                leastRequireTable = count
        
        return leastRequireTable

if __name__ == "__main__":
    print('=== Test Start ===')
    quiz = Solution()

    # Default quiz input situation: Return 3 tables
    # schedule = [
    #             ('13:00','14:00'),
    #             ('11:00','12:00'),
    #             ('11:30','12:30'),
    #             ('11:40','12:40')
    #             ]

    # Input situation 2: Return 4 tables
    # schedule = [
    #             ('13:00','14:00'),
    #             ('11:00','12:00'),
    #             ('11:30','12:30'),
    #             ('11:40','12:40'),
    #             ('11:35','12:20')
    #             ]

    # Input situation 3: Return 5 tables
    # schedule = [
    #             ('11:00','12:00'),
    #             ('11:30','12:30'),
    #             ('13:00','14:00'),
    #             ('11:40','12:40'),
    #             ('11:35','12:20'),
    #             ('11:32','12:25')
    #             ]

    # Very special input situation: Return 3 tables
    schedule = [
                ('11:00', '12:00'),
                ('11:00', '12:10'),
                ('12:30', '13:20'),
                ('13:00', '14:00'),
                ('11:40', '13:25'),
                ('12:25', '12:32')
                ]

    result = quiz.calculateMinTable(schedule)
    print('Calculate Min Table Result: ' + str(result))
    print('=== Test Over  ===')