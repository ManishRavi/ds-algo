/*
 * @lc app=leetcode id=61 lang=golang
 *
 * [61] Rotate List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	tail, count := head, 1
	// * Find the length of the linked list
	for tail.Next != nil {
		count++
		tail = tail.Next
	}

	k %= count
	if k == 0 {
		return head
	}

	// * Create a cycle by connecting the tail to the head of the linked list and find the new head after rotation by k places
	tail.Next = head
	stepsToNewHead := count - k
	for stepsToNewHead > 0 {
		stepsToNewHead--
		tail = tail.Next
	}

	head = tail.Next
	tail.Next = nil
	return head
}

// @lc code=end

