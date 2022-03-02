package main

func longestCommonPrefix(strs []string) string {
	if len(strs) <= 0 {
		return ""
	}

	firstString := strs[0]
	for i := range firstString {
		for j := 1; j < len(strs); j += 1 {
			if i >= len(strs[j]) || firstString[i] != strs[j][i] {
				return firstString[:i]
			}
		}
	}

	return firstString
}
