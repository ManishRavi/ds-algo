/*
 * @lc app=leetcode id=496 lang=golang
 *
 * [496] Next Greater Element I
 */

// @lc code=start
func nextGreaterElement(nums1 []int, nums2 []int) []int {
	res := []int{}
	for _, v1 := range nums1 {
		isElementFound, nextGreaterElement := false, -1
		for _, v2 := range nums2 {
			if v1 == v2 {
				isElementFound = true
			} else if isElementFound && v2 > v1 {
				nextGreaterElement = v2
				break
			}
		}

		res = append(res, nextGreaterElement)
	}

	return res
}

// @lc code=end

