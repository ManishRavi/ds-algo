package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil || l2 == nil {
		return l1
	}

	dummyHead, carry := ListNode{-1, nil}, 0
	cur := &dummyHead
	for l1 != nil || l2 != nil {
		l1Val, l2Val := 0, 0
		if l1 != nil {
			l1Val = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			l2Val = l2.Val
			l2 = l2.Next
		}

		carry += l1Val + l2Val
		cur.Next = &ListNode{carry % 10, nil}
		cur = cur.Next
		carry /= 10
	}

	if carry == 1 {
		cur.Next = &ListNode{1, nil}
	}

	return dummyHead.Next
}
