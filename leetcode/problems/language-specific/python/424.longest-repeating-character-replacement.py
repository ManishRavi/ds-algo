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
        s_counter = collections.defaultdict(int)
        max_count = 0
        longest_substring_length = 0
        left, right = 0, 0
        while right < len(s):
            max_count = max(max_count, s_counter[s[right]] + 1)
            window_length = right - left + 1
            # * Difference between window length and max count
            # * should be less than or equal to k
            # * (window_length - max_count <= k)
            if window_length - max_count <= k:
                s_counter[s[right]] += 1
                longest_substring_length = max(
                    longest_substring_length, window_length)
                right += 1

            else:
                s_counter[s[left]] -= 1
                left += 1

        return longest_substring_length

# @lc code=end
