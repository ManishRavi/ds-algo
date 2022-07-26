package main

/*
 * @lc app=leetcode id=34 lang=golang
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */

// @lc code=start

// * Binary Search Solution | O(logn) Time | O(1) Space
// * n -> Length of nums array

func searchRange(nums []int, target int) []int {
	if len(nums) <= 0 {
		return []int{-1, -1}
	}

	res, left, right := []int{-1, -1}, 0, len(nums)-1
	// * Find the first position by moving to the left, if the element is found
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] == target {
			res[0] = mid
			right = mid - 1
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	left, right = 0, len(nums)-1
	// * Find the last position by moving to the right, if the element is found
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] == target {
			res[1] = mid
			left = mid + 1
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return res
}

// @lc code=end
