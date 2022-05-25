package main

import "math"

// * Sliding Window Solution | O(m+n) Time | O(m+n) Space

func minWindow(s string, t string) string {
	sSize, tSize := len(s), len(t)
	if sSize <= 0 || tSize <= 0 || sSize < tSize {
		return ""
	}

	resIndexes, resLength := []int{-1, -1}, math.MaxInt32
	tMappings, windowMappings := map[rune]int{}, map[rune]int{}
	for _, v := range t {
		tMappings[v]++
	}

	have, need := 0, len(tMappings)
	left := 0
	for right, rightRune := range s {
		windowMappings[rightRune]++
		if _, ok := tMappings[rightRune]; ok && windowMappings[rightRune] == tMappings[rightRune] {
			have++
		}

		for have == need {
			if right-left+1 < resLength {
				resLength = right - left + 1
				resIndexes[0] = left
				resIndexes[1] = right
			}

			leftRune := rune(s[left])
			windowMappings[leftRune]--
			if _, ok := tMappings[leftRune]; ok && windowMappings[leftRune] < tMappings[leftRune] {
				have--
			}

			left++
		}
	}

	if resLength != math.MaxInt32 {
		left, right := resIndexes[0], resIndexes[1]
		return s[left : right+1]
	}

	return ""
}
