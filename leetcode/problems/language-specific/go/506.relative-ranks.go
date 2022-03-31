/*
 * @lc app=leetcode id=506 lang=golang
 *
 * [506] Relative Ranks
 */

// @lc code=start
func findRelativeRanks(score []int) []string {
	res, scoreCopy, placements := []string{}, make([]int, len(score)), map[int]int{}
	copy(scoreCopy, score)
	sort.Slice(scoreCopy, func(i, j int) bool {
		return scoreCopy[i] > scoreCopy[j]
	})

	for i, v := range scoreCopy {
		placements[v] = i + 1
	}

	for _, v := range score {
		switch placements[v] {
		case 1:
			res = append(res, "Gold Medal")
		case 2:
			res = append(res, "Silver Medal")
		case 3:
			res = append(res, "Bronze Medal")
		default:
			res = append(res, fmt.Sprintf("%v", placements[v]))
		}
	}

	return res
}

// @lc code=end

