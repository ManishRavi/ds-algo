package main

// * Math Solution | O(1) Time | O(1) Space

func countVowelStrings(n int) int {
	return (n + 4) * (n + 3) * (n + 2) * (n + 1) / 24
}

// * Backtracking Solution | O(n^5) Time | O(n) Space

func countVowelStringsBacktracking(n int) int {
	if n <= 0 {
		return 0
	}

	res := 0
	VOWELS := []byte{'a', 'e', 'i', 'o', 'u'}
	countVowelStringsBacktrackingHelper(n, 0, VOWELS, []byte{}, &res)
	return res
}

func countVowelStringsBacktrackingHelper(n, start int, VOWELS []byte, combination []byte, res *int) {
	if n == len(combination) {
		*res++
		return
	}

	for i := start; i < len(VOWELS); i++ {
		combination = append(combination, VOWELS[i])
		countVowelStringsBacktrackingHelper(n, i, VOWELS, combination, res)
		combination = combination[:len(combination)-1]
	}
}
