class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        find the most frequent letter, then once that is found
        find the contiounus string with k replacments via 
        vairiable sliding window
        """ 
        res = 0
        charSet = set(s)


        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res