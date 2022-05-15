/*
 * @lc app=leetcode id=41 lang=golang
 *
 * [41] First Missing Positive
 */

// @lc code=start

// * Three Pass Solution | O(n) Time | O(1) Space

func firstMissingPositive(nums []int) int {
	numsSize := len(nums)
	if numsSize <= 0 {
		return 1
	}

	// * Set all negative integers in the array to 0
	for i, v := range nums {
		if v < 0 {
			nums[i] = 0
		}
	}

	// * Mark the integers by negating in the array while looping through them
	for _, v := range nums {
		curVal := int(math.Abs(float64(v)))
		if curVal >= 1 && curVal <= numsSize {
			if nums[curVal-1] > 0 {
				nums[curVal-1] *= -1
			} else if nums[curVal-1] == 0 {
				nums[curVal-1] = -1 * (numsSize + 1)
			}
		}
	}

	// * Find the smallest missing positive integer
	for i := 1; i < numsSize+1; i++ {
		if nums[i-1] >= 0 {
			return i
		}
	}

	return numsSize + 1
}

// @lc code=end

