/*
 * @lc app=leetcode id=97 lang=golang
 *
 * [97] Interleaving String
 */

// @lc code=start

// * Bottom-Up Iterative Solution | O(mn) Time | O(mn) Space
// * m -> Length of s1 | n -> Length of s2

func isInterleave(s1 string, s2 string, s3 string) bool {
	s1Size, s2Size, s3Size := len(s1), len(s2), len(s3)
	if s1Size+s2Size != s3Size {
		return false
	}

	dp := make([][]bool, s1Size+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]bool, s2Size+1)
	}

	dp[s1Size][s2Size] = true
	for i := s1Size; i >= 0; i-- {
		for j := s2Size; j >= 0; j-- {
			if i < s1Size && s1[i] == s3[i+j] && dp[i+1][j] {
				dp[i][j] = true
			}
			if j < s2Size && s2[j] == s3[i+j] && dp[i][j+1] {
				dp[i][j] = true
			}
		}
	}

	return dp[0][0]
}

// @lc code=end

