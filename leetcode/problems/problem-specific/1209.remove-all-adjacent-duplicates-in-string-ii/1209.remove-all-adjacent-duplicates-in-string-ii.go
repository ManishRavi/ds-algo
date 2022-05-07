package main

import "strings"

// * O(n) Time | O(n) Space

type Pair struct {
	Key   rune
	Count int
}

func removeDuplicates(s string, k int) string {
	sSize := len(s)
	if sSize <= 0 || k == 0 || sSize < k {
		return s
	}

	stack := []Pair{}
	for _, v := range s {
		// * Increment the count of the existing last character Pair in the stack
		if len(stack) > 0 && stack[len(stack)-1].Key == v {
			stack[len(stack)-1].Count++
		} else {
			// * Push the new current character Pair to the stack
			stack = append(stack, Pair{v, 1})
		}

		// * Pop the last Pair from the stack if it repeats k times
		if stack[len(stack)-1].Count == k {
			stack = stack[:len(stack)-1]
		}
	}

	// * Build the final string from the stack
	var sb strings.Builder
	for _, v := range stack {
		for i := 0; i < v.Count; i++ {
			sb.WriteString(string(v.Key))
		}
	}

	return sb.String()
}
