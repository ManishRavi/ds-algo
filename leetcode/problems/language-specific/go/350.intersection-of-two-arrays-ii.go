/*
 * @lc app=leetcode id=350 lang=golang
 *
 * [350] Intersection of Two Arrays II
 */

// @lc code=start
func intersect(nums1 []int, nums2 []int) []int {
	res := []int{}
	sort.Ints(nums1)
	sort.Ints(nums2)
	i, j := 0, 0
	for i < len(nums1) && j < len(nums2) {
		if nums1[i] < nums2[j] {
			i++
		} else if nums2[j] < nums1[i] {
			j++
		} else {
			res = append(res, nums1[i])
			i++
			j++
		}
	}

	return res
}

// @lc code=end

