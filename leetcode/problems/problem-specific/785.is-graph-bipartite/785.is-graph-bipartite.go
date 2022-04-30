package main

func isBipartite(graph [][]int) bool {
	if len(graph) <= 0 {
		return false
	}

	ROWS := len(graph)
	parents := []int{}
	for i := 0; i < ROWS; i++ {
		parents = append(parents, i)
	}

	var find func(n int) int
	find = func(n int) int {
		for n != parents[n] {
			parents[n] = parents[parents[n]]
			n = parents[n]
		}

		return n
	}

	var union func(n1, n2 int)
	union = func(n1, n2 int) {
		parent1, parent2 := find(n1), find(n2)
		if parent1 != parent2 {
			parents[parent1] = parent2
		}
	}

	for i := 0; i < ROWS; i++ {
		for _, v := range graph[i] {
			if find(i) == find(v) {
				return false
			}

			union(v, graph[i][0])
		}
	}

	return true
}
