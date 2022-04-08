/*
 * @lc app=leetcode id=6 lang=golang
 *
 * [6] Zigzag Conversion
 */

// @lc code=start
func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}

	res, rowSlice, curRow, goingDown := "", make([]string, findMin(numRows, len(s))), 0, false
	for _, v := range s {
		rowSlice[curRow] += string(v)
		if curRow == 0 || curRow == numRows-1 {
			goingDown = !goingDown
		}
		if goingDown {
			curRow++
		} else {
			curRow--
		}
	}

	for _, v := range rowSlice {
		res += v
	}

	return res
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}

// @lc code=end

