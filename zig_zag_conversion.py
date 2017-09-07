class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """



        new_s = []
        if numRows == 1 or len(s) == 1 or numRows >= len(s):
            return s
        if numRows == 2:
            t = s[::2]
            m = s[1::2]
            for x in t:
                new_s.append(x)
            for y in m:
                new_s.append(y)

            return "".join(new_s)


        new_s = []
        for i in range(numRows):
            if i == 0:
                for x in s[::2*numRows-2]:
                    new_s.append(x)
            elif i == numRows -1:
                for x in s[numRows-1::2*numRows-2]:
                    new_s.append(x)
            else:
                m = s[i::2*numRows-2]
                n = s[2*numRows-2 -i::2*numRows-2]
                if len(m) == len(n):
                    for i in range(len(m)):
                        new_s.append(m[i])
                        new_s.append(n[i])
                else:
                    for i in range(len(m)):
                        new_s.append(m[i])
                        if i <= len(n) -1:
                            new_s.append(n[i])

        return  "".join(new_s)
