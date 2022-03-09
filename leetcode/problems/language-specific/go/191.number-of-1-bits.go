/*
 * @lc app=leetcode id=191 lang=golang
 *
 * [191] Number of 1 Bits
 */

// @lc code=start
func hammingWeight(num uint32) int {
	count := uint32(0)
	for i := 0; i < 32; i++ {
		count += num & 1
		num >>= 1
	}

	return int(count)
}

// @lc code=end

