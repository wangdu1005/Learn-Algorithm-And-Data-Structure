'''
Interviewee: Wangdu Lin
Email: wangdu1005@gmail.com
Test Date Time: 2018/03/26 10:00:00 AM
Programming Lauange: Python 2.7.10
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:

    '''
    Idea of solution:
    My idea is that append the left and right bracket into different stack 
    while looping the string also check the next letters,
    if the next letter is right bracket, which means it match the pair condition, 
    then I pop left and right stack in the same time and pairs plus 1 count.
    The main goal is to make sure all two stack in the end should be empty, 
    otherwise, this string is not fully pairs with left right bracket.
    Also, need to check other special situation, such as '))(a)b(d)e(g)'.
    '''
    def parenthesisCount(self, strData):
        # Confirm the legality of this input data
        if strData is None:
            return -1

        if strData == '':
            return 0

        leftStack = []
        rightStack = []
        pairsCount = 0
        # for loop ---> Time: O(n)
        for inx in range(len(strData)):
            cha = strData[inx]

            # stack append ---> Space: O(n)
            if cha == '(':
                leftStack.append(inx)
            elif cha == ')':
                rightStack.append(inx)
                if len(leftStack) > 0:
                    # pop() ---> Time: O(1)
                    leftStack.pop()
                    rightStack.pop()
                    pairsCount += 1

        if (len(leftStack) > 0 or len(rightStack) > 0):
            pairsCount = -1

        return pairsCount

if __name__ == "__main__":
    print('=== Test Start ===')
    quiz = Solution()

    # strData = None                             # print -1
    # strData = ''                               # print 0
    # strData = '(a)(b)()c'                      # print 3
    # strData = 'sdfsdfasdfasfhghg'              # print 0
    # strData = ')sdkfjsldkfgf('                 # print -1
    # strData = 'sdkfj(sldkfgf'                  # print -1
    # strData = '))a((b)(c)()d((((sf)s()))))'    # print -1, Becasue the inx 0, 1 right brackets missing two left brackets.
    strData = input("What is your string input for testing parenthesisCount? ")
    print('Input String: ' + str(strData))
    result = quiz.parenthesisCount(strData)
    print('Parenthesis Count: ' + str(result))
    print('=== Test Over  ===')