#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        lst=[]
        while x!=0:
            lst.append(x%10)
            x//=10
        i,j=0,len(lst)-1
        while i<=j:
            if lst[i]!=lst[j]:
                return False
            i+=1
            j-=1
        return True
# @lc code=end

