package main

func lengthOfLongestSubstring(s string) int {
	var exists = struct{}{}
	res, hashSet, left, right := 0, make(map[byte]struct{}), 0, 0
	for right < len(s) {
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
