package main

// * Bit Masking Solution | O(n^2) Time | O(n) Space

func maxProduct(words []string) int {
	res, wordsSize := 0, len(words)
	mask := make([]int, wordsSize)
	for i, word := range words {
		for _, v := range word {
			mask[i] |= 1 << (v - 'a')
		}

		for j := 0; j < i; j++ {
			if mask[i]&mask[j] == 0 {
				res = findMax(res, len(word)*len(words[j]))
			}
		}
	}

	return res
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
