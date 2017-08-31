class Solution(object):



    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if self.is_palindrome(s):
            return s

        return self.r_all_str(s)



    def is_palindrome(self,s):
        if s[0] != s[-1]:
            return False

        if s == s[::-1]:
            return True
        else:
            return False


    def r_all_str(self,s):
        '''返还 s 字符串所有可能的字符串切割 并按长度长到短排序'''
        lenth = len(s)
        for i in range(1,lenth+1)[::-1]: # 返回几位数
            if i == lenth:
                pass
            for j in range(lenth-i+1):
                if self.is_palindrome(s[j:i+j]):
                    return s[j:i+j]
        return None
