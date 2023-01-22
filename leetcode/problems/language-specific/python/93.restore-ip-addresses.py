#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start

# * Backtracking Solution | O(n*(3^n)) Time | O(n) Space
# * n -> The length of s string


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res

        def helper(start_idx, octets):
            if len(octets) == 4 and start_idx == len(s):
                res.append(".".join(octets))
                return

            for i in range(start_idx, min(start_idx + 3, len(s))):
                octet = s[start_idx : i + 1]
                if (
                    len(octets) >= 4
                    or len(octet) > 1
                    and (octet[0] == "0" or int(octet) > 255)
                ):
                    continue

                helper(i + 1, octets + [octet])

        helper(0, [])
        return res


# @lc code=end
