/*
 * @lc app=leetcode id=49 lang=golang
 *
 * [49] Group Anagrams
 */

// @lc code=start
func groupAnagrams(strs []string) [][]string {
	if len(strs) <= 0 {
		return [][]string{}
	}

	res, mappings := [][]string{}, map[string][]string{}
	for _, v := range strs {
		characterMappings := make([]int, 26)
		for _, v1 := range v {
			characterMappings[v1-'a']++
		}

		keyString := ""
		for _, v1 := range characterMappings {
			keyString += string(v1)
		}

		mappings[keyString] = append(mappings[keyString], v)
	}

	for _, v := range mappings {
		res = append(res, v)
	}

	return res
}

// @lc code=end

