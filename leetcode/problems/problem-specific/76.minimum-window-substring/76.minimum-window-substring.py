#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start

# * Two Pointers and Sliding Window Solution | O(m+n) Time | O(m+n) Space
# * m -> The length of s string | n -> The length of t string

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_length, t_length = len(s), len(t)
        if t_length > s_length:
            return ""

        t_counter = collections.Counter(t)
        window_counter = collections.defaultdict(int)
        have, need = 0, len(t_counter)
        min_window_range, min_window_length = [-1, -1], sys.maxsize
        left = 0

        # * Expand the window by moving the right pointer
        # * until we find a substring that has all the chars of t
        for right, right_val in enumerate(s):
            window_counter[right_val] += 1
            if right_val in t_counter and window_counter[right_val] == t_counter[right_val]:
                have += 1

            # * Contract the window by moving the left pointer
            # * till we've a substring that has all the chars of t
            while have == need:
                cur_window_length = right - left + 1
                if cur_window_length < min_window_length:
                    min_window_range = [left, right]
                    min_window_length = cur_window_length

                left_val = s[left]
                window_counter[left_val] -= 1
                if left_val in t_counter and window_counter[left_val] < t_counter[left_val]:
                    have -= 1

                left += 1

        left, right = min_window_range
        return s[left: right+1] if min_window_length != sys.maxsize else ""

# @lc code=end