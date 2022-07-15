package main

/*
 * @lc app=leetcode id=105 lang=golang
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
 */

// @lc code=start

// * Recursive Solution | O(n) Time | O(n) Space
// * n -> Number of nodes in a tree

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	curPreorderIndex, inorderMappings := 0, map[int]int{}
	// * Build a hashmap to store value -> index relations
	for i, v := range inorder {
		inorderMappings[v] = i
	}

	var buildTreeHelper func(left, right int) *TreeNode
	buildTreeHelper = func(left, right int) *TreeNode {
		// * If there are no elements to construct the tree
		if left > right {
			return nil
		}

		rootElement := preorder[curPreorderIndex]
		curPreorderIndex++
		root := &TreeNode{
			rootElement,
			buildTreeHelper(left, inorderMappings[rootElement]-1),
			buildTreeHelper(inorderMappings[rootElement]+1, right),
		}

		return root
	}

	return buildTreeHelper(0, len(preorder)-1)
}

// @lc code=end
