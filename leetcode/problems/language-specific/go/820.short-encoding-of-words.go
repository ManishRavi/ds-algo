/*
 * @lc app=leetcode id=820 lang=golang
 *
 * [820] Short Encoding of Words
 */

// @lc code=start

// * Iterative Store Prefix Solution | O(w^2) Time | O(w) Space

func minimumLengthEncoding(words []string) int {
	wordsSize := len(words)
	if wordsSize <= 0 {
		return 0
	}

	var exists = struct{}{}
	mappings := map[string]struct{}{}
	for _, v := range words {
		mappings[v] = exists
	}

	for _, v := range words {
		for i := 1; i < len(v); i++ {
			delete(mappings, v[i:])
		}
	}

	res := 0
	for k := range mappings {
		res += len(k) + 1
	}

	return res
}

// @lc code=end

