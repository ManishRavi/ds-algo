package main

func containsNearbyDuplicate(nums []int, k int) bool {
	if len(nums) <= 1 {
		return false
	}

	mappings := map[int]int{}
	for i, v := range nums {
		if mappings[v] > 0 && i-mappings[v] < k {
			return true
		}

		mappings[v] = i + 1
	}

	return false
}
