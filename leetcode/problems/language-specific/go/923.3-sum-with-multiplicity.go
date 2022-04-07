/*
 * @lc app=leetcode id=923 lang=golang
 *
 * [923] 3Sum With Multiplicity
 */

// @lc code=start
func threeSumMulti(arr []int, target int) int {
	mappings := map[int]int{}
	res := 0
	for i := 0; i < len(arr)-1; i++ {
		for j := i + 1; j < len(arr); j++ {
			diff := target - (arr[i] + arr[j])
			res += mappings[diff]
		}

		mappings[arr[i]]++
	}

	return res % int(1e9+7)
}

// @lc code=end

