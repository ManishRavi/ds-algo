package main

func toHex(num int) string {
	if num == 0 {
		return "0"
	}
	// * To handle negative integers
	if num < 0 {
		num += 1 << 32
	}

	res := ""
	for num != 0 {
		rem := num % 16
		if rem < 10 {
			res = string(48+rem) + res
		} else {
			res = string(87+rem) + res
		}

		num /= 16
	}

	return res
}
