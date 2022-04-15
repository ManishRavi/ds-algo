/*
 * @lc app=leetcode id=22 lang=golang
 *
 * [22] Generate Parentheses
 */

// @lc code=start
func generateParenthesis(n int) []string {
	res := []string{}
	generateParenthesisHelper(n, &res, "", 0, 0)
	return res
}

func generateParenthesisHelper(n int, res *[]string, cur string, open, close int) {
	if len(cur) == n*2 {
		*res = append(*res, cur)
		return
	}

	if open < n {
		generateParenthesisHelper(n, res, cur+"(", open+1, close)
	}

	if close < open {
		generateParenthesisHelper(n, res, cur+")", open, close+1)
	}
}

// @lc code=end

