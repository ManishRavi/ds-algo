package main

// * Sliding Window Solution | O(n) Time | O(n) Space

func lengthOfLongestSubstring(s string) int {
	sSize := len(s)
	if sSize <= 1 {
		return sSize
	}

	var exists = struct{}{}
	res, hashSet := 0, make(map[byte]struct{})
	left, right := 0, 0
	for right < sSize {
		if _, ok := hashSet[s[right]]; !ok {
			hashSet[s[right]] = exists
			res = findMax(res, len(hashSet))
			right++
		} else {
			delete(hashSet, s[left])
			left++
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
