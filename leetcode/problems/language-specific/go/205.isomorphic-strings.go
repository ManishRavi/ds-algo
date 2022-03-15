/*
 * @lc app=leetcode id=205 lang=golang
 *
 * [205] Isomorphic Strings
 */

// @lc code=start
func isIsomorphic(s string, t string) bool {
	a1 := [128]int{}
	a2 := [128]int{}
	for i := 0; i < len(s); i++ {
		if a1[s[i]] != a2[t[i]] {
			return false
		}

		a1[s[i]] = i + 1
		a2[t[i]] = i + 1
	}

	return true
}

// @lc code=end

