package main

// * Iterative Solution | O(n) Time | O(1) Space

func minPartitions(n string) int {
	largestDigit := 0
	for _, v := range n {
		largestDigit = findMax(largestDigit, int(v-'0'))
	}

	return largestDigit
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
