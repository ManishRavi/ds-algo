package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// * Post-Order DFS Traversal Solution | O(n) Time | O(h) Space

const (
	COVERED      = 0
	PLEASE_COVER = 1
	HAS_CAMERA   = 2
)

func minCameraCover(root *TreeNode) int {
	minCameras := 0
	var postOrder func(root *TreeNode) int
	postOrder = func(root *TreeNode) int {
		if root == nil {
			return COVERED
		}

		left, right := postOrder(root.Left), postOrder(root.Right)
		if left == PLEASE_COVER || right == PLEASE_COVER {
			minCameras++
			return HAS_CAMERA
		} else if left == HAS_CAMERA || right == HAS_CAMERA {
			return COVERED
		} else {
			return PLEASE_COVER
		}
	}

	if postOrder(root) == PLEASE_COVER {
		return minCameras + 1
	}

	return minCameras
}
