package main

// * Bottom-Up Iterative Solution | O(mn) Time | O(mn) Space

func minDistance(word1 string, word2 string) int {
	word1Size, word2Size := len(word1), len(word2)
	if word1Size == 0 && word2Size == 0 {
		return 0
	}

	ROWS, COLS := word2Size+1, word1Size+1 // * Include empty chatacters in both the words
	dp := make([][]int, ROWS)
	for i := 0; i < ROWS; i++ {
		dp[i] = make([]int, COLS)
	}

	// * Fill the 1st Column
	for i := 0; i < ROWS; i++ {
		dp[i][0] = i
	}
	// * Fill the 1st Row
	for j := 0; j < COLS; j++ {
		dp[0][j] = j
	}

	for i := 1; i < ROWS; i++ {
		for j := 1; j < COLS; j++ {
			// * If the characters don't match then find the minimum of 3 operations and add 1 for the current action
			// * else get the previous value ignoring current character
			if word1[j-1] != word2[i-1] {
				dp[i][j] = 1 + findMin(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
			} else {
				dp[i][j] = dp[i-1][j-1]
			}
		}
	}

	return dp[ROWS-1][COLS-1]
}

func findMin(a, b, c int) int {
	if a <= b && a <= c {
		return a
	} else if b <= a && b <= c {
		return b
	}

	return c
}
