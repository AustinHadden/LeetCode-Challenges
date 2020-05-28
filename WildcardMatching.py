class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 0th index -> 0th character
        # 1st index -> 1st character
        # Etc...
        match = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # 0 characters in s matches 0 characters in p
        match[0][0] = True

        # Consider all cases where all the '*' in p match 0 characters in 's'
        for p_i in range(len(p)):
            match[p_i + 1][0] = match[p_i][0] and p[p_i] == '*'
        
        for p_i in range(len(p)):
            for s_i in range(len(s)):
                # 1. Identical character in s and p + Match previous case
                # 2. Single wildcard '?' in p (any character in s) + Match previous case
                # 3. '*' matches 1 character on current iteration (and potentially more on next iteration)
                # 4. '*' matches 0 characters on current iteration
                match[p_i + 1][s_i + 1] = \
                    (s[s_i] == p[p_i] and match[p_i][s_i]) or \
                    (p[p_i] == '?' and match[p_i][s_i]) or \
                    (p[p_i] == '*' and match[p_i][s_i + 1]) or \
                    (p[p_i] == '*' and match[p_i + 1][s_i])                

        return match[-1][-1]