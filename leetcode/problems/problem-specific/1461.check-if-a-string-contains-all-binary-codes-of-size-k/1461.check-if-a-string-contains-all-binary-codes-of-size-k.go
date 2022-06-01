package main

// * Hashmap Based Solution | O(nk) Time | O(2^k) Space

func hasAllCodes(s string, k int) bool {
	sSize := len(s)
	if k > sSize {
		return false
	}

	var exists = struct{}{}
	mappings := map[string]struct{}{}
	for i := 0; i <= sSize-k; i++ {
		mappings[s[i:i+k]] = exists
		if len(mappings) == 1<<k {
			return true
		}
	}

	return false
}
