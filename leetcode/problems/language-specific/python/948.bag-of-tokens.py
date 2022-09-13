#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start

# * Sorting and Two Pointers Solution | O(nlogn) Time | O(1) Space
# * n -> The length of tokens array


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # * Sort in ascending order.
        tokens.sort()
        cur_score = max_score = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                cur_score += 1
                max_score = max(max_score, cur_score)
                left += 1
            elif cur_score >= 1:
                cur_score -= 1
                power += tokens[right]
                right -= 1
            else:
                break

        return max_score


# @lc code=end
