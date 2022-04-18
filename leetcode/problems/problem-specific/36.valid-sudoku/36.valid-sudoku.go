package main

import "fmt"

func isValidSudoku(board [][]byte) bool {
	if len(board) <= 0 {
		return false
	}

	var exists = struct{}{}
	mappings := make(map[string]struct{}, 0)
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			curVal := string(board[i][j])
			if curVal != "." {
				rowMapping := fmt.Sprintf("%vr%v", curVal, i)
				colMapping := fmt.Sprintf("%vc%v", curVal, j)
				boxMapping := fmt.Sprintf("%vb%v%v", curVal, i/3, j/3)
				_, rowMappingOk := mappings[rowMapping]
				_, colMappingOk := mappings[colMapping]
				_, boxMappingOk := mappings[boxMapping]
				if rowMappingOk || colMappingOk || boxMappingOk {
					return false
				}

				mappings[rowMapping] = exists
				mappings[colMapping] = exists
				mappings[boxMapping] = exists
			}
		}
	}

	return true
}
