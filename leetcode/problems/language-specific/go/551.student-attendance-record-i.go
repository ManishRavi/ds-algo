/*
 * @lc app=leetcode id=551 lang=golang
 *
 * [551] Student Attendance Record I
 */

// @lc code=start
func checkRecord(s string) bool {
	absentCount := 0
	for i := range s {
		if s[i] == 'A' {
			absentCount++
			if absentCount > 1 {
				return false
			}
		} else if s[i] == 'L' && i > 1 && s[i-1] == 'L' && s[i-2] == 'L' {
			return false
		}
	}

	return true
}

// @lc code=end

