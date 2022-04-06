/*
 * @lc app=leetcode id=3 lang=golang
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	var exists = struct{}{}
	res, hashSet, left, right := 0, make(map[byte]struct{}), 0, 0
	for right < len(s) {
		if _, ok := hashSet[s[right]]; !ok {
			hashSet[s[right]] = exists
			res = findMax(res, len(hashSet))
			right++
		} else {
			delete(hashSet, s[left])
			left++
		}
	}

	return res
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end

