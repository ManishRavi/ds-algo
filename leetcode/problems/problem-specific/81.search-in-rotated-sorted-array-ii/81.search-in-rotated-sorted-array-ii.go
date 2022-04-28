package main

func search(nums []int, target int) bool {
	if len(nums) <= 0 {
		return false
	}

	left, right := 0, len(nums)-1
	for left <= right {
		// * To avoid duplicates
		for left < right && nums[left] == nums[left+1] {
			left++
		}
		for right > left && nums[right] == nums[right-1] {
			right--
		}

		mid := left + (right-left)/2
		if nums[mid] == target {
			return true
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

	return false
}
