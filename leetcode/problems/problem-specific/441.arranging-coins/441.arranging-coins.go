package main

func arrangeCoins(n int) int {
	if n <= 2 {
		return 1
	}

	currentRow := 1
	for n >= currentRow {
		n -= currentRow
		currentRow++
	}

	return currentRow - 1
}
