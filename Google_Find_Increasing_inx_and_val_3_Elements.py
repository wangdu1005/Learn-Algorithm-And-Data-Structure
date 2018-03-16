# Hello World program in Python
class Solution:
    round = 0
    def checkElements(self, input):
        lenList = []
        maxLen = 0
        for i in range(len(input)):
            self.round += 1
            print("=======")
            print("Round: " + str(self.round))

            lenList.append(1)
            print("inx: " + str(i) + ", val:" + str(input[i]))
            print("---- loop in i by j ----")
            for j in range(i):
                if input[i] > input[j]:
                    print("Previous lenList: " + str(lenList))
                    print("inx i: " + str(i) + ", i.val: " + str(input[i]))
                    print("inx j: " + str(j) + ", j.val: " + str(input[j]))
                    lenList[i] = max(lenList[i], lenList[j] + 1)
                    print("Updated lenList: " + str(lenList))
                    print("----------------")
                    maxLen = max(lenList[i], maxLen)
                    if maxLen == 3:
                        return True
        return False

# data = [1, 3, 5, 2, 3, 4] # Return True
data = [1, 10, 4, 5]
# data = [1, 2, 1, 1, 3, 1] # Return True
# data = [1, 2, 1, 1, 1, 1] # Return False
# data = [5, 3, 1] # Return False

sol = Solution()
result = sol.checkElements(data)
print("===== Function Over =====")
print(result)

# ========= RUNTIME LOG ===========
# =======
# Round: 1
# inx: 0, val:1
# ---- loop in i by j ----
# =======
# Round: 2
# inx: 1, val:10
# ---- loop in i by j ----
# Previous lenList: [1, 1]
# inx i: 1, i.val: 10
# inx j: 0, j.val: 1
# Updated lenList: [1, 2]
# ----------------
# =======
# Round: 3
# inx: 2, val:4
# ---- loop in i by j ----
# Previous lenList: [1, 2, 1]
# inx i: 2, i.val: 4
# inx j: 0, j.val: 1
# Updated lenList: [1, 2, 2]
# ----------------
# =======
# Round: 4
# inx: 3, val:5
# ---- loop in i by j ----
# Previous lenList: [1, 2, 2, 1]
# inx i: 3, i.val: 5
# inx j: 0, j.val: 1
# Updated lenList: [1, 2, 2, 2]
# ----------------
# Previous lenList: [1, 2, 2, 2]
# inx i: 3, i.val: 5
# inx j: 2, j.val: 4
# Updated lenList: [1, 2, 2, 3]
# ----------------
# ===== Function Over =====
# True