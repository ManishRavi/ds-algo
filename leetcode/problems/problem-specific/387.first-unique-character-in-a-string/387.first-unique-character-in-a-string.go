package main

func firstUniqChar(s string) int {
	if len(s) == 1 {
		return 0
	}

	mappings := [26]int{}
	for _, v := range s {
		mappings[int(v-'a')]++
	}

	for i, v := range s {
		if mappings[int(v-'a')] == 1 {
			return i
		}
	}

	return -1
}
