#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic={'}':'{',']':'[',')':'('}
        lst=[]
        for i in s:
            if i not in dic:
                lst.append(i)
            else:
                if not lst or lst[-1]!=dic[i]:
                    return False
                else:
                    lst.pop()
        return True if not lst else False
# @lc code=end

