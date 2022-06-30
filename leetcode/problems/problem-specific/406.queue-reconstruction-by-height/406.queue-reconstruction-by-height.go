package main

import "sort"

// * Sorting Based Solution | O(n^2) Time | O(1) Space

func reconstructQueue(people [][]int) [][]int {
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] == people[j][0] {
			return people[i][1] < people[j][1]
		}

		return people[i][0] > people[j][0]
	})

	reconstructedQueue := make([][]int, len(people))
	for _, v := range people {
		copy(reconstructedQueue[v[1]+1:], reconstructedQueue[v[1]:])
		reconstructedQueue[v[1]] = v
	}

	return reconstructedQueue
}
