/*
 * @lc app=leetcode id=349 lang=golang
 *
 * [349] Intersection of Two Arrays
 */

// @lc code=start
func intersection(nums1 []int, nums2 []int) []int {
	var exists = struct{}{}
	s1, s2, res := make(map[int]struct{}), make(map[int]struct{}), make(map[int]struct{})
	for _, v := range nums1 {
		s1[v] = exists
	}
	for _, v := range nums2 {
		s2[v] = exists
	}

	// * Better to iterate over a shorter set
	if len(s1) > len(s2) {
		s1, s2 = s2, s1
	}

	for k := range s1 {
		if _, ok := s2[k]; ok {
			res[k] = exists
		}
	}

	resSlice := []int{}
	for k := range res {
		resSlice = append(resSlice, k)
	}

	return resSlice
}

// @lc code=end

