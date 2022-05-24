package main

// * Bottom-Up Iterative Solution | O(mnk) Time | O(mn) Space

func findMaxForm(strs []string, m int, n int) int {
	dp := make([][]int, m+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, n+1)
	}

	var countZeroesAndOnes func(s string) []int
	countZeroesAndOnes = func(s string) []int {
		counters := make([]int, 2)
		for _, v := range s {
			counters[v-'0']++
		}

		return counters
	}

	for _, v := range strs {
		counters := countZeroesAndOnes(v)
		for i := m; i >= counters[0]; i-- {
			for j := n; j >= counters[1]; j-- {
				dp[i][j] = findMax(dp[i][j], 1+dp[i-counters[0]][j-counters[1]])
			}
		}
	}

	return dp[m][n]
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
