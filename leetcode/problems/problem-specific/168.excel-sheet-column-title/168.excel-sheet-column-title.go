package main

func convertToTitle(columnNumber int) string {
	res := ""
	for columnNumber > 0 {
		columnNumber--
		res = string(65+(columnNumber)%26) + res
		columnNumber /= 26
	}

	return res
}
