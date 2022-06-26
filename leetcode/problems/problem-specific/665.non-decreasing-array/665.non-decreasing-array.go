package main

// * Iterative Solution | O(n) Time | O(1) Space

func checkPossibility(nums []int) bool {
	numsSize := len(nums)
	if numsSize <= 2 {
		return true
	}

	elementModified := false
	for i := 0; i < numsSize-1; i++ {
		if nums[i] <= nums[i+1] {
			continue
		}
		if elementModified {
			return false
		}

		// * Modifiy the element
		if i == 0 || nums[i+1] >= nums[i-1] {
			nums[i] = nums[i+1]
		} else {
			nums[i+1] = nums[i]
		}

		elementModified = true
	}

	return true
}
