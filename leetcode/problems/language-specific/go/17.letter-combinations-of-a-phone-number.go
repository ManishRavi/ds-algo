/*
 * @lc app=leetcode id=17 lang=golang
 *
 * [17] Letter Combinations of a Phone Number
 */

// @lc code=start

// * Backtracking Solution | O(4^n) Time | O(n) Space

func letterCombinations(digits string) []string {
	if len(digits) <= 0 {
		return []string{}
	}

	MAPPINGS := []string{"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
	res := []string{}
	letterCombinationsHelper(digits, MAPPINGS, &res, "", 0)
	return res
}

func letterCombinationsHelper(digits string, MAPPINGS []string, res *[]string, combination string, index int) {
	if index == len(digits) {
		*res = append(*res, combination)
		return
	}

	letters := MAPPINGS[digits[index]-'0']
	for _, v := range letters {
		letterCombinationsHelper(digits, MAPPINGS, res, combination+string(v), index+1)
	}
}

// @lc code=end

