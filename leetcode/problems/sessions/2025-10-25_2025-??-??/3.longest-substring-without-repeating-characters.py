#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start

# * Two Pointers and Sliding Window Solution | O(n) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        longest_substring_len = 0
        left = right = 0
        while right < len(s):
            if s[right] not in s_set:
                s_set.add(s[right])
                longest_substring_len = max(longest_substring_len, len(s_set))
                right += 1
            else:
                s_set.remove(s[left])
                left += 1

        return longest_substring_len


# @lc code=end
