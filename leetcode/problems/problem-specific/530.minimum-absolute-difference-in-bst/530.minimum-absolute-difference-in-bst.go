package main

import "math"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getMinimumDifference(root *TreeNode) int {
	minDifferenceVal, slice := math.MaxInt64, []int{}
	inOrderTraversal(root, &slice)
	for i := 1; i < len(slice); i++ {
		minDifferenceVal = findMin(minDifferenceVal, int(math.Abs(float64(slice[i])-float64(slice[i-1]))))
	}

	return minDifferenceVal
}

func inOrderTraversal(root *TreeNode, slice *[]int) {
	if root == nil {
		return
	}

	inOrderTraversal(root.Left, slice)
	*slice = append(*slice, root.Val)
	inOrderTraversal(root.Right, slice)
}

func findMin(a, b int) int {
	if a <= b {
		return a
	}

	return b
}
