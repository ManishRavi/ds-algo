package main

func generate(numRows int) [][]int {
	if numRows == 0 {
		return [][]int{}
	}

	res := [][]int{{1}}
	for i := 2; i <= numRows; i++ {
		prev := res[len(res)-1]
		cur := []int{}
		for j := 0; j < i; j++ {
			cur = append(cur, 1)
		}
		for j := 1; j < i-1; j++ {
			cur[j] = prev[j-1] + prev[j]
		}

		res = append(res, cur)
	}

	return res
}
