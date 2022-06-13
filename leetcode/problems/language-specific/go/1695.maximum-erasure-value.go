/*
 * @lc app=leetcode id=1695 lang=golang
 *
 * [1695] Maximum Erasure Value
 */

// @lc code=start

// * Sliding Window Solution | O(n) Time | O(c) Space

func maximumUniqueSubarray(nums []int) int {
	numsSize := len(nums)
	if numsSize <= 0 {
		return 0
	}

	mappings := make([]int, 10001)
	curScore, maxScore := 0, 0
	for left, right := 0, 0; right < numsSize; right++ {
		curScore += nums[right]
		mappings[nums[right]]++
		for mappings[nums[right]] > 1 {
			curScore -= nums[left]
			mappings[nums[left]]--
			left++
		}

		maxScore = findMax(maxScore, curScore)
	}

	return maxScore
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end

