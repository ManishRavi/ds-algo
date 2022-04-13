package main

func gameOfLife(board [][]int) {
	// To keep track after changing an element:
	// If it changed from 1 to 0, then we’ll replace it with 2, so any value greater than 1 is equal to 1
	// And in case 0 to 1, then we’ll replace it with -1, so any value smaller 0 is equal to 0

	m, n := len(board), len(board[0])
	for row := range board {
		for col := range board[row] {
			// Finding 8 neighbors
			totalLiveNeighbors := 0
			// Vertical
			if row > 0 && board[row-1][col] >= 1 {
				totalLiveNeighbors++
			}
			if row < m-1 && board[row+1][col] >= 1 {
				totalLiveNeighbors++
			}

			// Horizontal
			if col > 0 && board[row][col-1] >= 1 {
				totalLiveNeighbors++
			}
			if col < n-1 && board[row][col+1] >= 1 {
				totalLiveNeighbors++
			}

			// Diagonal
			// 1. Top Diagonal
			if row > 0 && col > 0 && board[row-1][col-1] >= 1 {
				totalLiveNeighbors++
			}
			if row > 0 && col < n-1 && board[row-1][col+1] >= 1 {
				totalLiveNeighbors++
			}

			// 2. Bottom Diagonal
			if row < m-1 && col > 0 && board[row+1][col-1] >= 1 {
				totalLiveNeighbors++
			}
			if row < m-1 && col < n-1 && board[row+1][col+1] >= 1 {
				totalLiveNeighbors++
			}

			// Set the next state
			// If it's a live cell
			if board[row][col] == 1 {
				if totalLiveNeighbors < 2 || totalLiveNeighbors > 3 {
					board[row][col] = 2
				}
			} else { // If it's a dead cell
				if totalLiveNeighbors == 3 {
					board[row][col] = -1
				}
			}
		}
	}

	for row := range board {
		for col := range board[row] {
			if board[row][col] == 2 {
				board[row][col] = 0
			} else if board[row][col] == -1 {
				board[row][col] = 1
			}
		}
	}
}

func gameOfLifeWithoutInPlace(board [][]int) {
	m, n := len(board), len(board[0])
	res := make([][]int, m)
	for i := 0; i < m; i++ {
		res[i] = make([]int, n)
		copy(res[i], board[i])
	}

	for row := range board {
		for col := range board[row] {
			// Finding 8 neighbors
			totalLiveNeighbors := 0
			// Vertical
			if row > 0 && board[row-1][col] == 1 {
				totalLiveNeighbors++
			}
			if row < m-1 && board[row+1][col] == 1 {
				totalLiveNeighbors++
			}

			// Horizontal
			if col > 0 && board[row][col-1] == 1 {
				totalLiveNeighbors++
			}
			if col < n-1 && board[row][col+1] == 1 {
				totalLiveNeighbors++
			}

			// Diagonal
			// 1. Top Diagonal
			if row > 0 && col > 0 && board[row-1][col-1] == 1 {
				totalLiveNeighbors++
			}
			if row > 0 && col < n-1 && board[row-1][col+1] == 1 {
				totalLiveNeighbors++
			}

			// 2. Bottom Diagonal
			if row < m-1 && col > 0 && board[row+1][col-1] == 1 {
				totalLiveNeighbors++
			}
			if row < m-1 && col < n-1 && board[row+1][col+1] == 1 {
				totalLiveNeighbors++
			}

			// Set the next state
			// If it's a live cell
			if board[row][col] == 1 {
				if totalLiveNeighbors < 2 || totalLiveNeighbors > 3 {
					res[row][col] = 0
				}
			} else { // If it's a dead cell
				if totalLiveNeighbors == 3 {
					res[row][col] = 1
				}
			}
		}
	}

	copy(board, res)
}
