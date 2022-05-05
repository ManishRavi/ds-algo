package main

import "sort"

// * O(nlog(n)) Time | O(1) Space

func maxOperations(nums []int, k int) int {
	numsSize := len(nums)
	if numsSize <= 1 {
		return 0
	}

	res := 0
	left, right := 0, numsSize-1
	sort.Ints(nums)
	for left < right {
		currentSum := nums[left] + nums[right]
		if currentSum == k {
			res++
			left++
			right--
		} else if currentSum < k {
			left++
		} else {
			right--
		}
	}

	return res
}
