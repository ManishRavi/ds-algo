package main

func exist(board [][]byte, word string) bool {
	if len(board) <= 0 || len(board[0]) <= 0 ||
		len(word) <= 0 || len(board)*len(board[0]) < len(word) {
		return false
	}

	ROWS, COLS := len(board), len(board[0])
	var existHelper func(row, col, pos int) bool
	existHelper = func(row, col, pos int) bool {
		if pos == len(word) {
			return true
		}
		if row < 0 || col < 0 ||
			row >= ROWS || col >= COLS ||
			board[row][col] != word[pos] ||
			board[row][col] == '*' {
			return false
		}

		prevBoardVal := board[row][col]
		board[row][col] = '*'
		found := existHelper(row+1, col, pos+1) ||
			existHelper(row-1, col, pos+1) ||
			existHelper(row, col+1, pos+1) ||
			existHelper(row, col-1, pos+1)
		board[row][col] = prevBoardVal
		return found
	}

	for row := 0; row < ROWS; row++ {
		for col := 0; col < COLS; col++ {
			if existHelper(row, col, 0) {
				return true
			}
		}
	}

	return false
}
