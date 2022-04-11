/*
 * @lc app=leetcode id=682 lang=golang
 *
 * [682] Baseball Game
 */

// @lc code=start
func calPoints(ops []string) int {
	res, stack := 0, []int{}
	for _, v := range ops {
		switch v {
		case "+":
			stack = append(stack, stack[len(stack)-2]+stack[len(stack)-1])
		case "D":
			stack = append(stack, 2*stack[len(stack)-1])
		case "C":
			stack = stack[:len(stack)-1]
		default:
			vInt, _ := strconv.Atoi(v)
			stack = append(stack, vInt)
		}
	}
	for _, v := range stack {
		res += v
	}

	return res
}

// @lc code=end

