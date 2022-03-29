/*
 * @lc app=leetcode id=455 lang=golang
 *
 * [455] Assign Cookies
 */

// @lc code=start
func findContentChildren(g []int, s []int) int {
	if len(s) == 0 {
		return 0
	}

	count, i, j := 0, 0, 0
	sort.Ints(g)
	sort.Ints(s)
	for i < len(g) && j < len(s) {
		if s[j] >= g[i] {
			count++
			i++
		}

		j++
	}

	return count
}

// @lc code=end

