/*
 * @lc app=leetcode id=10 lang=golang
 *
 * [10] Regular Expression Matching
 */

// @lc code=start

// * O(nm) Time | O(nm) Space

func isMatch(s string, p string) bool {
	// * Top-down memoization approach
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

		matchCondition := i < len(s) && (s[i] == p[j] || p[j] == '.')
		if j+1 < len(p) && p[j+1] == '*' {
			// * Either don't use "*" --> (i, j+2) or use "*" --> (i+1, j)
			memcache[fmt.Sprintf("%v_%v", i, j)] = isMatchHelperDFS(i, j+2) ||
				(matchCondition && isMatchHelperDFS(i+1, j))
			return memcache[fmt.Sprintf("%v_%v", i, j)]
		}

		// * If both chars match
		if matchCondition {
			memcache[fmt.Sprintf("%v_%v", i, j)] = isMatchHelperDFS(i+1, j+1)
			return memcache[fmt.Sprintf("%v_%v", i, j)]
		}

		memcache[fmt.Sprintf("%v_%v", i, j)] = false
		return memcache[fmt.Sprintf("%v_%v", i, j)]
	}

	return isMatchHelperDFS(0, 0)
}

// @lc code=end

