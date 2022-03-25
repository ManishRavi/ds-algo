/*
 * @lc app=leetcode id=387 lang=golang
 *
 * [387] First Unique Character in a String
 */

// @lc code=start
func firstUniqChar(s string) int {
	if len(s) == 1 {
		return 0
	}

	mappings := [26]int{}
	for _, v := range s {
		mappings[int(v-'a')]++
	}

	for i, v := range s {
		if mappings[int(v-'a')] == 1 {
			return i
		}
	}

	return -1
}

// @lc code=end

