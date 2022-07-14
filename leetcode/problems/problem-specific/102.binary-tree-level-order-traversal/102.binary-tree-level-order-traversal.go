package main

/*
 * @lc app=leetcode id=102 lang=golang
 *
 * [102] Binary Tree Level Order Traversal
 */

// @lc code=start

// * Iterative BFS Solution | O(n) Time | O(n) Space
// * n -> Number of nodes in a tree

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	res, queue := [][]int{}, []*TreeNode{root}
	for len(queue) > 0 {
		curQueueSize, curLevelElements := len(queue), []int{}
		for i := 0; i < curQueueSize; i++ {
			curNode := queue[0]
			queue = queue[1:]
			curLevelElements = append(curLevelElements, curNode.Val)
			if curNode.Left != nil {
				queue = append(queue, curNode.Left)
			}
			if curNode.Right != nil {
				queue = append(queue, curNode.Right)
			}
		}

		res = append(res, curLevelElements)
	}

	return res
}

// @lc code=end
