/*
 * @lc app=leetcode id=389 lang=golang
 *
 * [389] Find the Difference
 */

// @lc code=start
func findTheDifference(s string, t string) byte {
	if len(s) <= 0 {
		return byte(t[0])
	}

	mappings := [26]int{}
	for _, v := range s {
		mappings[int(v-'a')]++
	}

	var res byte
	for _, v := range t {
		mappings[int(v-'a')]--
		if mappings[int(v-'a')] < 0 {
			res = byte(v)
			break
		}
	}

	return res
}

// @lc code=end

