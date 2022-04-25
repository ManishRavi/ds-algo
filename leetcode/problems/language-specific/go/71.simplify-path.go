/*
 * @lc app=leetcode id=71 lang=golang
 *
 * [71] Simplify Path
 */

// @lc code=start
func simplifyPath(path string) string {
	stack := []string{}
	pathSplit := strings.Split(path, "/")
	for _, v := range pathSplit {
		if len(stack) > 0 && v == ".." {
			stack = stack[:len(stack)-1]
		} else if v != "." && v != ".." && v != "" {
			stack = append(stack, v)
		}
	}

	return fmt.Sprintf("/%v", strings.Join(stack, "/"))
}

// @lc code=end

