/*
 * @lc app=leetcode id=86 lang=golang
 *
 * [86] Partition List
 */

// @lc code=start

// * Two Pointer Solution | O(n) Time | O(1) Space
// * n -> Number of nodes in a linked list

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func partition(head *ListNode, x int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	smallerDummyHead, biggerDummyHead := &ListNode{0, nil}, &ListNode{0, nil}
	curSmaller, curBigger := smallerDummyHead, biggerDummyHead
	for head != nil {
		if head.Val < x {
			curSmaller.Next = head
			curSmaller = curSmaller.Next
		} else {
			curBigger.Next = head
			curBigger = curBigger.Next
		}

		head = head.Next
	}

	// * Attach the head of a bigger node to the tail of a smaller node
	curSmaller.Next = biggerDummyHead.Next
	// * Remove the duplicate link from the tail of a bigger node
	curBigger.Next = nil

	return smallerDummyHead.Next
}

// @lc code=end

