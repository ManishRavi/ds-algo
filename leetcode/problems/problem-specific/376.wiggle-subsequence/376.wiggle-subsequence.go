package main

// * Greedy Solution | O(n) Time | O(1) Space
// * n -> Length of the nums array

func wiggleMaxLength(nums []int) int {
	numsSize := len(nums)
	if numsSize <= 1 {
		return numsSize
	}

	prevDiff, longestWiggleSubsequence := nums[1]-nums[0], 2
	// * If prevDiff is zero consider only 1 element as both the elements are same
	if prevDiff == 0 {
		longestWiggleSubsequence = 1
	}

	for i := 2; i < numsSize; i++ {
		curDiff := nums[i] - nums[i-1]
		if (prevDiff >= 0 && curDiff < 0) || (prevDiff <= 0 && curDiff > 0) {
			prevDiff = curDiff
			longestWiggleSubsequence++
		}
	}

	return longestWiggleSubsequence
}
