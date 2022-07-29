package main

/*
 * @lc app=leetcode id=242 lang=golang
 *
 * [242] Valid Anagram
 */

// @lc code=start

// * Hash Table Solution | O(n) Time | O(1) Space
// * n -> Number of letters in s/t

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	letterMappings := [256]int{}
	for _, v := range t {
		letterMappings[v]++
	}

	for _, v := range s {
		letterMappings[v]--
		if letterMappings[v] < 0 {
			return false
		}
	}

	return true
}

// @lc code=end
