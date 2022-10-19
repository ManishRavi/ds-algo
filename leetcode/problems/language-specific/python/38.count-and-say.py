#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start

# * Iterative Solution | O(nm) Time | O(m) Space
# * n -> The given input | m -> The length of string


class Solution:
    def countAndSay(self, n: int) -> str:
        res = ["1"]
        n -= 1
        while n:
            cur_val = []
            i = 0
            while i < len(res):
                cur_count = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    cur_count += 1
                    i += 1

                cur_val.extend([str(cur_count), res[i]])
                i += 1

            res = cur_val
            n -= 1

        return "".join(res)


# @lc code=end
