/*
 * @lc app=leetcode id=461 lang=golang
 *
 * [461] Hamming Distance
 */

// @lc code=start
func hammingDistance(x int, y int) int {
	count := 0
	for i := 0; i < 32; i++ {
		count += (x & 1) ^ (y & 1)
		x >>= 1
		y >>= 1
	}

	return count
}

// @lc code=end

