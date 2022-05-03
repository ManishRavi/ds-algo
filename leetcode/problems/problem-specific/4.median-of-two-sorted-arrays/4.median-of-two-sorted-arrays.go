package main

import "math"

// * O(log(min(m, n))) Time | O(1) Space

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	if len(nums2) < len(nums1) {
		nums1, nums2 = nums2, nums1
	}

	nums1Size, nums2Size := len(nums1), len(nums2)
	totalSize := nums1Size + nums2Size
	left, right := 0, nums1Size
	for left <= right {
		partition1 := left + (right-left)/2
		partition2 := (totalSize+1)/2 - partition1

		left1, left2 := math.MinInt64, math.MinInt64
		right1, right2 := math.MaxInt64, math.MaxInt64
		if partition1 > 0 {
			left1 = nums1[partition1-1]
		}
		if partition1 < nums1Size {
			right1 = nums1[partition1]
		}
		if partition2 > 0 {
			left2 = nums2[partition2-1]
		}
		if partition2 < nums2Size {
			right2 = nums2[partition2]
		}

		if left1 <= right2 && left2 <= right1 {
			if isEvenDigit(totalSize) {
				return float64((float64(findMax(left1, left2) + findMin(right1, right2))) / 2.0)
			} else {
				return float64(findMax(left1, left2))
			}
		} else if left1 > right2 {
			right = partition1 - 1
		} else {
			left = partition1 + 1
		}
	}

	return 0.0
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

func isEvenDigit(n int) bool {
	return n%2 == 0
}
