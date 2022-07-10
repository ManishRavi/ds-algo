/*
 * @lc app=leetcode id=1696 lang=golang
 *
 * [1696] Jump Game VI
 */

// @lc code=start

// * Monotonic Queue Solution | O(n) Time | O(k) Space
// * n -> Length of the nums array | k -> Maximum steps allowed

func maxResult(nums []int, k int) int {
	numsSize := len(nums)
	dq := []int{0}
	for i := 1; i < numsSize; i++ {
		nums[i] += nums[dq[0]]
		for len(dq) > 0 && nums[i] >= nums[dq[len(dq)-1]] {
			dq = dq[:len(dq)-1]
		}

		dq = append(dq, i)
		if i-dq[0] >= k {
			dq = dq[1:]
		}
	}

	return nums[numsSize-1]
}

// @lc code=end

