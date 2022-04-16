package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func trimBST(root *TreeNode, low int, high int) *TreeNode {
	if root == nil {
		return root
	}
	// * If node.val > high --> the trimmed binary tree occurs to the left of the node
	if root.Val > high {
		return trimBST(root.Left, low, high)
	}
	// * If node.val < low --> the trimmed binary tree occurs to the right of the node
	if root.Val < low {
		return trimBST(root.Right, low, high)
	}

	// * Otherwise, trim both sides of the tree
	root.Left = trimBST(root.Left, low, high)
	root.Right = trimBST(root.Right, low, high)
	return root
}
