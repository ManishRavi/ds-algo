package main

/*
 * @lc app=leetcode id=576 lang=golang
 *
 * [576] Out of Boundary Paths
 */

// @lc code=start

// * Recursive DFS Solution | O(mnk) Time | O(mnk) Space
// * m -> Total number of rows | n -> Total number of columns | k -> Maximum number of moves allowed

func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
	if maxMove <= 0 {
		return 0
	}

	DIRECTIONS := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	// * Build an empty cache
	memcache := make([][][]int, m)
	for i := range memcache {
		memcache[i] = make([][]int, n)
		for j := range memcache[i] {
			memcache[i][j] = make([]int, maxMove+1)
			for k := range memcache[i][j] {
				memcache[i][j][k] = -1
			}
		}
	}

	var findPathsHelper func(maxMove, startRow, startColumn int) int
	findPathsHelper = func(maxMove, startRow, startColumn int) int {
		if startRow < 0 || startRow > m-1 ||
			startColumn < 0 || startColumn > n-1 {
			return 1
		}
		if maxMove <= 0 {
			return 0
		}
		if memcache[startRow][startColumn][maxMove] != -1 {
			return memcache[startRow][startColumn][maxMove]
		}

		curPaths := 0
		for _, v := range DIRECTIONS {
			curRow, curColumn := v[0], v[1]
			curPaths += findPathsHelper(maxMove-1, startRow+curRow, startColumn+curColumn)
		}

		memcache[startRow][startColumn][maxMove] = curPaths % 1000000007
		return memcache[startRow][startColumn][maxMove]
	}

	return findPathsHelper(maxMove, startRow, startColumn)
}

// @lc code=end
