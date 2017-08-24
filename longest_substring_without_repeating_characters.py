class Solution(object):


    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenth = len(s)

        if "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ " in s:
            return len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ")

        if lenth > 0 :
            for num in range(0,len(s))[::-1]:
                n = 0
                while num+n < lenth:
                    mstr = s[n:num+n+1]
                    m = len(mstr)
                    j = 0
                    while j < m:
                        if mstr[j] in mstr[j+1:]:
                            break
                        else:
                            j = j +1
                            if j +1 == m:
                                return m
                    n = n + 1
            return 1
        else:
            return 0