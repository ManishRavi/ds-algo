/*
 * @lc app=leetcode id=412 lang=golang
 *
 * [412] Fizz Buzz
 */

// @lc code=start
func fizzBuzz(n int) []string {
	res := []string{}
	for i := 1; i <= n; i++ {
		switch {
		case i%3 == 0 && i%5 == 0:
			res = append(res, "FizzBuzz")

		case i%3 == 0:
			res = append(res, "Fizz")

		case i%5 == 0:
			res = append(res, "Buzz")

		default:
			res = append(res, fmt.Sprintf("%v", i))
		}
	}

	return res
}

// @lc code=end

