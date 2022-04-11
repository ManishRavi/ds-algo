package main

import "sort"

func threeSum(nums []int) [][]int {
	if len(nums) < 3 {
		return [][]int{}
	}

	res := [][]int{}
	sort.Ints(nums)
	for i := 0; i < len(nums)-1; i++ {
		left, right := i+1, len(nums)-1
		for left < right {
			totalSum := nums[i] + nums[left] + nums[right]
			if totalSum == 0 {
				triplet := []int{nums[i], nums[left], nums[right]}
				res = append(res, triplet)
				leftVal := nums[left]
				for left < len(nums) && nums[left] == leftVal {
					left++
				}
				rightVal := nums[right]
				for right > left && nums[right] == rightVal {
					right--
				}
			} else if totalSum < 0 {
				left++
			} else {
				right--
			}
		}

		for i+1 < len(nums)-1 && nums[i] == nums[i+1] {
			i++
		}
	}

	return res
}
