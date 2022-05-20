/*
 * @lc app=leetcode id=329 lang=golang
 *
 * [329] Longest Increasing Path in a Matrix
 */

// @lc code=start

// * Recursive DFS Memoization Solution | O(nm) Time | O(nm) Space

func longestIncreasingPath(matrix [][]int) int {
	ROWS, COLS := len(matrix), len(matrix[0])
	res, memcache := 0, map[string]int{}
	DIRECTIONS := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	var longestIncreasingPathHelperDFS func(row, col, prevVal int) int
	longestIncreasingPathHelperDFS = func(row, col, prevVal int) int {
		if row < 0 || col < 0 ||
			row >= ROWS || col >= COLS ||
			matrix[row][col] <= prevVal {
			return 0
		}
		if v, ok := memcache[fmt.Sprintf("%v_%v", row, col)]; ok {
			return v
		}

		curPathLength := 1
		for _, v := range DIRECTIONS {
			newRow, newCol := row+v[0], col+v[1]
			curPathLength = findMax(curPathLength, 1+longestIncreasingPathHelperDFS(newRow, newCol, matrix[row][col]))
		}

		memcache[fmt.Sprintf("%v_%v", row, col)] = curPathLength
		res = findMax(res, curPathLength)
		return curPathLength
	}

	for row := range matrix {
		for col := range matrix[row] {
			longestIncreasingPathHelperDFS(row, col, -1)
		}
	}

	return res
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

// @lc code=end

