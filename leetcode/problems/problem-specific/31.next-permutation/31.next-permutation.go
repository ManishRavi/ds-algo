package main

func nextPermutation(nums []int) {
	// * 1. Find the first decreasing element from the end
	i := len(nums) - 2
	for i >= 0 && nums[i] >= nums[i+1] {
		i--
	}

	// * 2. Find the next greater element for the decreasing element from the end
	if i >= 0 {
		j := len(nums) - 1
		for nums[i] >= nums[j] {
			j--
		}

		// * 3. Swap elements at i and j
		nums[i], nums[j] = nums[j], nums[i]
	}

	// * 4. Reverse the array from i+1 to end
	reverse(nums, i+1, len(nums)-1)
}

func reverse(nums []int, start, end int) {
	for start < end {
		nums[start], nums[end] = nums[end], nums[start]
		start++
		end--
	}
}
