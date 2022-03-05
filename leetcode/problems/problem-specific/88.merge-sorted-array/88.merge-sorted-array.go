package main

func merge(nums1 []int, m int, nums2 []int, n int) {
	if (m == 0 && n == 0) || n == 0 {
		return
	}

	m--
	n--
	for i := m + n + 1; i >= 0; i-- {
		if m >= 0 && n >= 0 && nums1[m] >= nums2[n] {
			nums1[i] = nums1[m]
			m--
		} else if n >= 0 {
			nums1[i] = nums2[n]
			n--
		}
	}
}
