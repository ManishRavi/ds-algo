/*
 * @lc app=leetcode id=1689 lang=golang
 *
 * [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
 */

// @lc code=start

// * Iterative Solution | O(n) Time | O(1) Space

func minPartitions(n string) int {
	largestDigit := 0
	for _, v := range n {
		largestDigit = findMax(largestDigit, int(v-'0'))
	}

	return largestDigit
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end

