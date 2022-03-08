/*
 * @lc app=leetcode id=119 lang=golang
 *
 * [119] Pascal's Triangle II
 */

// @lc code=start
func getRow(rowIndex int) []int {
	res := []int{1}
	for i := 1; i <= rowIndex; i++ {
		cur := []int{}
		for j := 0; j <= i; j++ {
			cur = append(cur, 1)
		}
		for j := 1; j < i; j++ {
			cur[j] = res[j-1] + res[j]
		}

		res = cur
	}

	return res
}

// @lc code=end

