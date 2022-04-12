package main

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	if len(nums) < 3 {
		return 0
	}

	closest := math.MaxInt32
	sort.Ints(nums)
	for i := 0; i < len(nums)-1; i++ {
		left, right := i+1, len(nums)-1
		for left < right {
			totalSum := nums[i] + nums[left] + nums[right]
			if int(math.Abs(float64(totalSum-target))) < int(math.Abs(float64(closest-target))) {
				closest = totalSum
			}
			if totalSum == target {
				return totalSum
			} else if totalSum < target {
				left++
			} else {
				right--
			}
		}
	}

	return closest
}
