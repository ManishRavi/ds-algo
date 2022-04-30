/*
 * @lc app=leetcode id=92 lang=golang
 *
 * [92] Reverse Linked List II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if head == nil || head.Next == nil || left == 0 || right == 0 {
		return head
	}

	dummyHead := &ListNode{0, head}
	prev := dummyHead
	for i := 0; i < left-1; i++ {
		prev = prev.Next
	}

	cur := prev.Next
	for left < right {
		next := cur.Next
		cur.Next = next.Next
		next.Next = prev.Next
		prev.Next = next
		left++
	}

	return dummyHead.Next
}

// @lc code=end

