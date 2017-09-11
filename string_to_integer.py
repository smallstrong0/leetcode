class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        # x_list = s.split(' ')
        # s = ''.join(x_list)


        if s == '':
            return 0





        if s[0:1] == '-':
            s = s[1:]
            t = []
            for i in s:
                if i  in ['0','1','2','3','4','5','6','7','8','9']:
                    t.append(i)
                else:
                    break

            s = ''.join(t)

            if s == '':
                return 0

            if int(s) > 2147483648:
                return -2147483648
            else:
                return -1 * int(s)
        else:
            if s[0:1] == '+':
                s = s[1:]
            t = []
            for i in s:
                if i  in ['0','1','2','3','4','5','6','7','8','9']:
                    t.append(i)
                else:
                    break

            s = ''.join(t)

            if s == '':
                return 0

            if int(s) > 2147483647:
                return 2147483647
            else:
                return int(s)
