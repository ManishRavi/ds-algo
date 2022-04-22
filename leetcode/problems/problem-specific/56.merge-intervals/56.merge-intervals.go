package main

import "sort"

func merge(intervals [][]int) [][]int {
	if len(intervals) <= 1 {
		return intervals
	}

	res, n, i := [][]int{}, len(intervals), 0
	// * Sort the intervals based on start value
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	for i = 0; i < n-1; i++ {
		start, end := intervals[i][0], intervals[i][1]
		for i < n-1 && end >= intervals[i+1][0] {
			end = findMax(end, intervals[i+1][1])
			i++
		}

		res = append(res, []int{start, end})
	}

	if i == n-1 {
		res = append(res, intervals[i])
	}

	return res
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
