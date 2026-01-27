from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)

        start, end = 0, 0
        min_length = len(s) + 1
        min_start = 0
        num_chars_left = len(t)

        while end < len(s):

            if s[end] in t_map:
                if t_map[s[end]] > 0:
                    num_chars_left -= 1
                t_map[s[end]] -= 1

            while num_chars_left == 0:
                if end - start + 1 < min_length:
                    min_start = start
                    min_length = end - start + 1

                if s[start] in t_map:
                    t_map[s[start]] += 1
                    if t_map[s[start]] > 0:
                        num_chars_left += 1

                start += 1

            end += 1

        if min_length == len(s) + 1:
            return ""
        else:
            return s[min_start:min_start+min_length]
