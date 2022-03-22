/*
 * @lc app=leetcode id=242 lang=golang
 *
 * [242] Valid Anagram
 */

// @lc code=start
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	countArray := [256]int{}
	for _, v := range t {
		countArray[v]++
	}

	for _, v := range s {
		countArray[v]--
		if countArray[v] < 0 {
			return false
		}
	}

	return true
}

// @lc code=end

