package main

func containsDuplicate(nums []int) bool {
	if len(nums) <= 1 {
		return false
	}

	mappings := map[int]int{}
	for _, v := range nums {
		mappings[v]++
		if mappings[v] > 1 {
			return true
		}
	}

	return false
}
