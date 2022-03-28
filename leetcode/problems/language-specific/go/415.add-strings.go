/*
 * @lc app=leetcode id=415 lang=golang
 *
 * [415] Add Strings
 */

// @lc code=start
func addStrings(num1 string, num2 string) string {
	res, i, j, totalSum := "", len(num1)-1, len(num2)-1, 0
	for i >= 0 || j >= 0 {
		if i >= 0 {
			totalSum += int(num1[i] - '0')
		}
		if j >= 0 {
			totalSum += int(num2[j] - '0')
		}

		res = fmt.Sprintf("%v%v", totalSum%10, res)
		totalSum /= 10
		i--
		j--
	}

	if totalSum != 0 {
		res = fmt.Sprintf("%v%v", totalSum%10, res)
	}

	return res
}

// @lc code=end

