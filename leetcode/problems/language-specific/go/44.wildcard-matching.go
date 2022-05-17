/*
 * @lc app=leetcode id=44 lang=golang
 *
 * [44] Wildcard Matching
 */

// @lc code=start

// * Top-down Memoization Solution | O(mn) Time | O(mn) Space

func isMatch(s string, p string) bool {
	memcache := map[string]bool{}
	var isMatchHelperDFS func(i, j int) bool
	isMatchHelperDFS = func(i, j int) bool {
		if v, ok := memcache[fmt.Sprintf("%v_%v", i, j)]; ok {
			return v
		}
		if i >= len(s) && j >= len(p) {
			return true
		}
		if j >= len(p) {
			return false
		}

		if p[j] == '*' {
			// * Either don't use "*" --> (i, j+1) or use "*" --> (i+1, j)
			memcache[fmt.Sprintf("%v_%v", i, j)] = isMatchHelperDFS(i, j+1) ||
				(i < len(s) && isMatchHelperDFS(i+1, j))
			return memcache[fmt.Sprintf("%v_%v", i, j)]
		}

		// * If both chars match
		if i < len(s) && (s[i] == p[j] || p[j] == '?') {
			memcache[fmt.Sprintf("%v_%v", i, j)] = isMatchHelperDFS(i+1, j+1)
			return memcache[fmt.Sprintf("%v_%v", i, j)]
		}

		memcache[fmt.Sprintf("%v_%v", i, j)] = false
		return memcache[fmt.Sprintf("%v_%v", i, j)]
	}

	return isMatchHelperDFS(0, 0)
}

// @lc code=end

