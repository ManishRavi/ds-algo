package main

// * Iterative BFS Solution | O(mn) Time | O(mn) Space

func shortestPathBinaryMatrix(grid [][]int) int {
	if grid[0][0] == 1 {
		return -1
	}

	ROWS, COLS := len(grid), len(grid[0])
	queue := [][]int{}
	queue = append(queue, []int{0, 0, 1}) // [row, col, length]
	grid[0][0] = 1
	dir := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}}
	for len(queue) > 0 {
		curSize := len(queue)
		for curSize > 0 {
			curCell := queue[0]
			queue = queue[1:]
			if curCell[0] == ROWS-1 && curCell[1] == COLS-1 {
				return curCell[2]
			}

			for _, v := range dir {
				row, col := curCell[0]+v[0], curCell[1]+v[1]
				if row >= 0 && row < ROWS && col >= 0 && col < COLS && grid[row][col] == 0 {
					queue = append(queue, []int{row, col, curCell[2] + 1})
					grid[row][col] = 1
				}
			}

			curSize--
		}
	}

	return -1
}
