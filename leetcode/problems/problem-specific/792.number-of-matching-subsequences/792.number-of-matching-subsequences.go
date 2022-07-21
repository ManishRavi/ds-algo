package main

/*
 * @lc app=leetcode id=792 lang=golang
 *
 * [792] Number of Matching Subsequences
 */

// @lc code=start

// * Iterative HashMap Solution | O(n*(wl)) Time | O(w) Space
// * n -> Length of s | w -> Number of words | l -> Length of each word

func numMatchingSubseq(s string, words []string) int {
	sSize := len(s)
	sMappings := make(map[byte][]string, sSize)
	res := 0
	for _, v := range s {
		vByte := byte(v)
		sMappings[vByte] = []string{}
	}
	for _, word := range words {
		startChar := word[0]
		if _, ok := sMappings[startChar]; ok {
			sMappings[startChar] = append(sMappings[startChar], word)
		}
	}

	for _, v := range s {
		curCharWords := sMappings[byte(v)]
		curCharWordsSize := len(curCharWords)
		for i := 0; i < curCharWordsSize; i++ {
			curWord := curCharWords[i]
			sMappings[byte(v)] = sMappings[byte(v)][1:]
			if len(curWord[1:]) == 0 {
				res++
			} else if _, ok := sMappings[curWord[1]]; ok {
				sMappings[curWord[1]] = append(sMappings[curWord[1]], curWord[1:])
			}
		}
	}

	return res
}

// @lc code=end
