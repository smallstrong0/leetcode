class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        level = {0}
        for i, c in enumerate(p[:-1], 1):
            if not level:
                return False

            if c == ".":
                if p[i] == "*":
                    level = set(range(min(level), len(s)+1))
                else:
                    level = {j+1 for j in level if j < len(s)}
            elif c != "*":
                if p[i] == "*":
                    tmp = set()
                    for j in level:
                        while j < len(s) and s[j] == c:
                            j += 1
                            tmp.add(j)
                    level.update(tmp)
                else:
                    level = {j+1 for j in level if j < len(s) and s[j] == c}

        if p[-1] == "*":
            return len(s) in level
        else:
            return len(s) - 1 in level and (s[-1] == p[-1] or "." == p[-1])




