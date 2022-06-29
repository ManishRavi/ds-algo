/*
 * @lc app=leetcode id=1647 lang=golang
 *
 * [1647] Minimum Deletions to Make Character Frequencies Unique
 */

// @lc code=start

// * Sorting Based Solution | O(n + klogk) Time | O(k) Space
// * n is the length of the given string and k is the maximum possible number of distinct characters in s

func minDeletions(s string) int {
	frequencies := make([]int, 26)
	for _, v := range s {
		frequencies[v-'a']++
	}

	sort.Slice(frequencies, func(i, j int) bool {
		return frequencies[i] > frequencies[j]
	})

	minCharsToDelete, minFrequencyAllowed := 0, frequencies[0]
	for _, v := range frequencies {
		if v > minFrequencyAllowed {
			minCharsToDelete += v
			if minFrequencyAllowed > 0 {
				minCharsToDelete -= minFrequencyAllowed
			}
		}

		minFrequencyAllowed = findMin(minFrequencyAllowed-1, v-1)
	}

	return minCharsToDelete
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}

// @lc code=end

