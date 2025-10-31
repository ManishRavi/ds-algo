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
        s_len, t_len = len(s), len(t)
        if t_len > s_len:
            return ""

        t_counter, window_counter = Counter(t), defaultdict(int)
        have_count, need_count = 0, len(t_counter)
        min_window_range, min_window_len = [-1, -1], float("inf")
        left = 0
        for right, right_val in enumerate(s):
            window_counter[right_val] += 1
            if (
                right_val in t_counter
                and window_counter[right_val] == t_counter[right_val]
            ):
                have_count += 1

            while have_count == need_count:
                cur_window_len = right - left + 1
                if cur_window_len < min_window_len:
                    min_window_range = [left, right]
                    min_window_len = cur_window_len

                left_val = s[left]
                window_counter[left_val] -= 1
                if (
                    left_val in t_counter
                    and window_counter[left_val] < t_counter[left_val]
                ):
                    have_count -= 1

                left += 1

        left, right = min_window_range
        return s[left : right + 1] if min_window_len != float("inf") else ""


# @lc code=end
