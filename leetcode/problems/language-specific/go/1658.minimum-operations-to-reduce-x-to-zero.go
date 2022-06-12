/*
 * @lc app=leetcode id=1658 lang=golang
 *
 * [1658] Minimum Operations to Reduce X to Zero
 */

// @lc code=start

// * Sliding Window Solution | O(n) Time | O(1) Space

func minOperations(nums []int, x int) int {
	numsSize := len(nums)
	target := getSliceSum(nums) - x
	windowSize, curSum := -1, 0
	for left, right := 0, 0; right < numsSize; right++ {
		curSum += nums[right]
		for curSum > target && left <= right {
			curSum -= nums[left]
			left++
		}

		if curSum == target {
			windowSize = findMax(windowSize, right-left+1)
		}
	}

	if windowSize == -1 {
		return windowSize
	}

	return numsSize - windowSize
}

func getSliceSum(nums []int) int {
	curSum := 0
	for _, v := range nums {
		curSum += v
	}

	return curSum
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end

