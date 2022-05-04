package main

import "math"

// * O(n) Time | O(1) Space

func findUnsortedSubarray(nums []int) int {
	numsSize := len(nums)
	if numsSize <= 1 {
		return 0
	}

	minVal, maxVal := math.MaxInt32, math.MinInt32
	// * Find the decreasing element from the start
	for i := 1; i < numsSize; i++ {
		if nums[i] < nums[i-1] {
			minVal = findMin(minVal, nums[i])
		}
	}

	// * Find the increasing element from the end
	for i := numsSize - 2; i >= 0; i-- {
		if nums[i] > nums[i+1] {
			maxVal = findMax(maxVal, nums[i])
		}
	}

	// * If array is already sorted
	if minVal == math.MaxInt32 && maxVal == math.MinInt32 {
		return 0
	}

	left, right := 0, numsSize-1
	// * Find the position from the left where element > minVal
	for ; left < numsSize; left++ {
		if nums[left] > minVal {
			break
		}
	}

	// * Find the position from the right where element < maxVal
	for ; right >= 0; right-- {
		if nums[right] < maxVal {
			break
		}
	}

	return right - left + 1
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b

}
