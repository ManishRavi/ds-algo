package main

func romanToInt(s string) int {
	if len(s) < 0 {
		return 0
	}

	romanSymbols := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	res, i, v1, v2 := 0, 0, 0, 0
	for i = 0; i < len(s)-1; i += 1 {
		v1 = romanSymbols[s[i]]
		v2 = romanSymbols[s[i+1]]
		if v2 > v1 {
			res += v2 - v1
			i += 1
		} else {
			res += v1
		}
	}

	if i == len(s) {
		return res
	}

	return res + romanSymbols[s[i]]
}
