package main

import (
	"fmt"
	"strings"
)

// * Math Solution | O(n^2) Time | O(n) Space

func getPermutation(n int, k int) string {
	var sb strings.Builder
	fact, nums := 1, []int{}
	for i := 1; i < n; i++ {
		fact *= i
		nums = append(nums, i)
	}

	nums = append(nums, n)
	k--
	for {
		curPos := int(k / fact)
		sb.WriteString(fmt.Sprintf("%v", nums[curPos]))
		nums = append(nums[:curPos], nums[curPos+1:]...)
		if len(nums) <= 0 {
			break
		}

		k %= fact
		fact /= len(nums)
	}

	return sb.String()
}
