package main

// * Bottom-Up Iterative Solution | O(mn) Time | O(mn) Space

func minDistance(word1 string, word2 string) int {
	word1Size, word2Size := len(word1), len(word2)
	if word1 == word2 {
		return 0
	}
	if word1Size <= 0 {
		return word2Size
	}
	if word2Size <= 0 {
		return word1Size
	}

	dp := make([][]int, word1Size+1)
	for i := range dp {
		dp[i] = make([]int, word2Size+1)
	}

	for i := 0; i <= word1Size; i++ {
		for j := 0; j <= word2Size; j++ {
			if i == 0 || j == 0 {
				dp[i][j] = i + j
			} else if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				dp[i][j] = 1 + findMin(dp[i-1][j], dp[i][j-1])
			}
		}
	}

	return dp[word1Size][word2Size]
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}
