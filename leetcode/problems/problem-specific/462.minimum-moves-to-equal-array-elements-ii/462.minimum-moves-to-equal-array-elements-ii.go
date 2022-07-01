package main

import (
	"math"
	"sort"
)

// * Sorting Based Solution | O(nlogn) Time | O(1) Space

func minMoves2(nums []int) int {
	numsSize := len(nums)
	sort.Ints(nums)
	midElement := nums[int(numsSize/2)]
	minMoves := 0
	for _, v := range nums {
		minMoves += int(math.Abs(float64(v - midElement)))
	}

	return minMoves
}
