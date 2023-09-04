class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = dict()
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        #print(dic)
        ans = 0
        anyNumOne = 0
        anyOdd = 0
        for k in dic:
            if dic[k] >= 2:
                if dic[k] % 2:
                    anyOdd = 1
                    ans += (dic[k] - 1)
                else:
                    ans += dic[k] 
            else:
                anyNumOne = 1
        if anyNumOne or anyOdd :
            ans = ans + 1
        return ans

# 思路: 將各個字母出現的次數記載dict, 找出出現次數>2的字元，將他們出現的次數以偶數做加總，
#       最後檢查是否曾經只出現過一次的字元，以及是否有出現奇數次的字元，如果有就將加總多加一