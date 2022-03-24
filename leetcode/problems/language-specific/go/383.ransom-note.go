/*
 * @lc app=leetcode id=383 lang=golang
 *
 * [383] Ransom Note
 */

// @lc code=start
func canConstruct(ransomNote string, magazine string) bool {
	if len(ransomNote) > len(magazine) {
		return false
	}

	mappings := [26]int{}
	for _, v := range magazine {
		mappings[int(v-'a')]++
	}

	for _, v := range ransomNote {
		mappings[int(v-'a')]--
		if mappings[int(v-'a')] < 0 {
			return false
		}
	}

	return true
}

// @lc code=end

// * This is slower
func canConstructHashMapApproach(ransomNote string, magazine string) bool {
	if len(ransomNote) > len(magazine) {
		return false
	}

	mappings := map[byte]int{}
	for _, v := range magazine {
		mappings[byte(v)]++
	}

	for _, v := range ransomNote {
		mappings[byte(v)]--
		if mappings[byte(v)] < 0 {
			return false
		}
	}

	return true
}
