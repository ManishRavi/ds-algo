package main

import "sort"

func fourSum(nums []int, target int) [][]int {
	if len(nums) < 4 {
		return [][]int{}
	}

	res := [][]int{}
	sort.Ints(nums)
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			left, right := j+1, len(nums)-1
			for left < right {
				totalSum := nums[i] + nums[j] + nums[left] + nums[right]
				if totalSum == target {
					quadruplet := []int{nums[i], nums[j], nums[left], nums[right]}
					res = append(res, quadruplet)
					leftVal := nums[left]
					for left < len(nums) && nums[left] == leftVal {
						left++
					}

					rightVal := nums[right]
					for right > left && nums[right] == rightVal {
						right--
					}
				} else if totalSum < target {
					left++
				} else {
					right--
				}
			}

			for j+1 < len(nums) && nums[j] == nums[j+1] {
				j++
			}
		}

		for i+1 < len(nums) && nums[i] == nums[i+1] {
			i++
		}
	}

	return res
}
