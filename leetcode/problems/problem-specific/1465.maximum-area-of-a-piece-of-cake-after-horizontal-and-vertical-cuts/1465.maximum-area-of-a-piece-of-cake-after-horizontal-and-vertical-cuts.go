package main

import "sort"

// * Sorting Based Solution | O(hlogh) + O(wlogw) Time | O(1) Space
// * h -> Total Height, w -> Total Width

func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
	sort.Ints(horizontalCuts)
	sort.Ints(verticalCuts)
	maxHorizontalDiff, maxVerticalDiff := findMaxDiff(h, horizontalCuts), findMaxDiff(w, verticalCuts)
	return (maxHorizontalDiff * maxVerticalDiff) % 1000000007
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func findMaxDiff(maxSize int, cuts []int) int {
	cutsSize := len(cuts)
	maxDiff := cuts[0]
	for i := 1; i < cutsSize; i++ {
		maxDiff = findMax(maxDiff, cuts[i]-cuts[i-1])
	}

	maxDiff = findMax(maxDiff, maxSize-cuts[cutsSize-1])
	return maxDiff
}
