# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["Wangdu Lin, jiuzhang"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wangdu Lin"
__email__ = "wangdu1005@gmail.com"
__status__ = "Production"

class Solution:
    # @param {string} source a source string
    # @param {string} target a target string
    # @return {int} an integer as index
    def strStr2(self, source, target):
        # Write your code here
        if source is None or target is None:
            return -1
        m = len(target)
        n = len(source)

        if m == 0:
            return 0

        import random
        mod = random.randint(1000000, 2000000)
        hash_target = 0
        m26 = 1

        for i in xrange(m):
            hash_target = (hash_target * 26 + ord(target[i]) - ord('a')) % mod
            if hash_target < 0:
                hash_target += mod

        for i in xrange(m - 1):
            m26 = m26 * 26 % mod

        value = 0
        for i in xrange(n):
            if i >= m:
                value = (value - m26 * (ord(source[i - m]) - ord('a'))) % mod

            value = (value * 26 + ord(source[i]) - ord('a')) % mod
            if value < 0:
                value += mod

            if i >= m - 1 and value == hash_target:
                return i - m + 1

        return -1