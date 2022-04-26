package main

func sortColors(nums []int) {
	if len(nums) <= 0 {
		return
	}

	left, mid, right := 0, 0, len(nums)-1
	for mid <= right {
		switch nums[mid] {
		case 0:
			nums[left], nums[mid] = nums[mid], nums[left]
			left++
			mid++

		case 1:
			mid++

		case 2:
			nums[mid], nums[right] = nums[right], nums[mid]
			right--
		}
	}
}
