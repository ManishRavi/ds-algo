#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start

# * Two Pointers and Sliding Window Solution | O(n) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_counter = defaultdict(int)
        max_count = longest_substring_len = 0
        left = right = 0
        while right < len(s):
            window_len = right - left + 1
            max_count = max(max_count, s_counter[s[right]] + 1)
            if window_len - max_count <= k:
                s_counter[s[right]] += 1
                longest_substring_len = max(longest_substring_len, window_len)
                right += 1
            else:
                s_counter[s[left]] -= 1
                left += 1

        return longest_substring_len


# @lc code=end
