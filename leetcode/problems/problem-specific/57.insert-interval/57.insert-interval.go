package main

func insert(intervals [][]int, newInterval []int) [][]int {
	if len(intervals) <= 0 {
		return [][]int{{newInterval[0], newInterval[1]}}
	}

	insertPosition := findInsertPosition(intervals, newInterval)
	// * Switch elements to the right
	intervals = append(intervals, []int{})
	copy(intervals[insertPosition+1:], intervals[insertPosition:])
	intervals[insertPosition] = newInterval

	return merge(intervals)
}

func findInsertPosition(intervals [][]int, newInterval []int) int {
	i, n := 0, len(intervals)
	// To handle TC --> intervals = [[1,4]], newInterval = [0,5]
	if n <= 1 {
		if newInterval[0] >= intervals[0][0] {
			return 1
		}

		return 0
	}

	for i = 0; i < n-1; i++ {
		// To handle TC --> intervals = [[1,5],[6,8]], newInterval = [0,9]
		if i == 0 && newInterval[0] <= intervals[i][0] {
			return i
		} else if newInterval[0] >= intervals[i][0] && newInterval[0] < intervals[i+1][0] {
			break
		}
	}

	return i + 1
}

func merge(intervals [][]int) [][]int {
	if len(intervals) <= 1 {
		return intervals
	}

	res, n, i := [][]int{}, len(intervals), 0
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
