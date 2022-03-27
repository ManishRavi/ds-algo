package main

func longestPalindrome(s string) int {
	if len(s) == 1 {
		return 1
	}

	mappings, isOddLettersDone, res := map[byte]int{}, false, 0
	for _, v := range s {
		mappings[byte(v)]++
	}

	for _, v := range mappings {
		// * In case of odd count
		if v%2 != 0 {
			if !isOddLettersDone {
				isOddLettersDone = true
			} else {
				// * Add (count or v)-1 from the second odd character onwards. So, decrementing the res by 1 as we're adding the (count or v) at the end of the block
				res -= 1
			}
		}

		res += v
	}

	return res
}
