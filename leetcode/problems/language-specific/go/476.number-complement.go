/*
 * @lc app=leetcode id=476 lang=golang
 *
 * [476] Number Complement
 */

// @lc code=start
func findComplement(num int) int {
	// 1. Convert num to it's binary string
	// 2. Count the number of bits in num
	// 3. Make mask of 1s of the same length
	// 4. XOR the num and mask
	return num ^ ((1 << len(strconv.FormatInt(int64(num), 2))) - 1)
}

// @lc code=end

