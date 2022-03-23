/*
 * @lc app=leetcode id=290 lang=golang
 *
 * [290] Word Pattern
 */

// @lc code=start
func wordPattern(pattern string, s string) bool {
	sSplit := strings.Split(s, " ")
	if len(pattern) != len(sSplit) {
		return false
	}

	patternMappings := map[byte]string{}
	sMappings := map[string]byte{}
	for i := range pattern {
		_, ok1 := patternMappings[pattern[i]]
		_, ok2 := sMappings[sSplit[i]]

		if !ok1 && !ok2 {
			patternMappings[pattern[i]] = sSplit[i]
			sMappings[sSplit[i]] = pattern[i]
		} else if patternMappings[pattern[i]] != sSplit[i] || sMappings[sSplit[i]] != pattern[i] {
			return false
		}
	}

	return true
}

// @lc code=end

