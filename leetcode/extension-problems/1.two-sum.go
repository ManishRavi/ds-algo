/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	res := []int{-1, -1}
	if len(nums) < 2 {
		return res
	}

	hashMap := map[int]int{}
	other := 0
	for i := range nums {
		other = target - nums[i]
		if _, ok := hashMap[other]; ok {
			res[0] = hashMap[other]
			res[1] = i
		}

		hashMap[nums[i]] = i
	}

	return res
}

// @lc code=end

