/*
 * @lc app=leetcode id=717 lang=golang
 *
 * [717] 1-bit and 2-bit Characters
 */

// @lc code=start
func isOneBitCharacter(bits []int) bool {
	/** Algorithm
	  1. Traverse with an index i: if bits[i] == 0, increase by 1, else by 2
	  2. If reached the end, check and return if last bit is 0 or 1
	  3. If the loop did not return anything, then it means the last char was double,
	     terminating the index. If it's double char, then return false.
	*/

	i := 0
	for i < len(bits) {
		if i == len(bits)-1 {
			return bits[i] == 0
		}

		i += bits[i] + 1 // if bits[i] = 0 --> (0+1), else bits[i] = 1 --> (1+1)
	}

	return false
}

// @lc code=end

