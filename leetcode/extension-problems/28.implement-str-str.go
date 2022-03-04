/*
 * @lc app=leetcode id=28 lang=golang
 *
 * [28] Implement strStr()
 */

// @lc code=start
func strStr(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}

	haystackLength := len(haystack)
	needleLength := len(needle)
	if haystackLength <= 0 || needleLength <= 0 || needleLength > haystackLength {
		return -1
	}

	for i := 0; i <= haystackLength-needleLength; i++ {
		j := 0
		for j = 0; j < needleLength; j++ {
			if haystack[i+j] != needle[j] {
				break
			}
		}
		if j == needleLength {
			return i
		}
	}

	return -1
}

// @lc code=end

