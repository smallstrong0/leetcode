class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        try:
            if x > 0:
                i = int(str(x)[::-1])
                if i > 2147483647:
                    return 0
                else:
                    return i
            else:
                x = abs( x )
                i = int(str(x)[::-1])
                if i > 2147483647:
                    return 0
                else:
                    return -i
        except Exception, e:
            return 0