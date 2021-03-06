package main

func search(nums []int, target int) int {
	if len(nums) <= 0 {
		return -1
	}

	left, right := 0, len(nums)-1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] == target {
			return mid
		} else if nums[left] <= nums[mid] { // * If left half is sorted
			// * find if target lies on left half or not
			if target >= nums[left] && target <= nums[mid] {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else { // * If right half is sorted
			// * find if target lies on right half or not
			if target >= nums[mid] && target <= nums[right] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}

	return -1
}
