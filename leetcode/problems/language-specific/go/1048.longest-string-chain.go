/*
 * @lc app=leetcode id=1048 lang=golang
 *
 * [1048] Longest String Chain
 */

// @lc code=start

// * Bottom-Up Iterative Solution | O(nlogn) + O(n^2*16) Time | O(n) Space

func longestStrChain(words []string) int {
	wordsSize := len(words)
	if wordsSize <= 1 {
		return wordsSize
	}

	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) < len(words[j])
	})

	maxWordChain := 0
	dp := make([]int, wordsSize)
	for i := range dp {
		dp[i] = 1
	}

	for i := 1; i < wordsSize; i++ {
		for j := 0; j < i; j++ {
			if isValidPredecessor(words[i], words[j]) {
				dp[i] = findMax(dp[i], 1+dp[j])
			}
		}

		maxWordChain = findMax(maxWordChain, dp[i])
	}

	return maxWordChain
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

func isValidPredecessor(w1, w2 string) bool {
	w1Size, w2Size := len(w1), len(w2)
	if w1Size != w2Size+1 {
		return false
	}

	i, j := 0, 0
	for i < w1Size {
		if j < w2Size && w1[i] == w2[j] {
			i++
			j++
		} else {
			i++
		}
	}

	if i == w1Size && j == w2Size {
		return true
	}

	return false
}

// @lc code=end

