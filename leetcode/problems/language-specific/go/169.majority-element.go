/*
 * @lc app=leetcode id=169 lang=golang
 *
 * [169] Majority Element
 */

// @lc code=start
func majorityElement(nums []int) int {
	res := 0
	size := int(math.Floor(float64(len(nums) / 2)))
	mappings := map[int]int{}
	for _, v := range nums {
		mappings[v]++
		if mappings[v] > size {
			res = v
			break
		}
	}

	return res
}

// @lc code=end

