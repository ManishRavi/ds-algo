package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	dummyHead := &ListNode{0, head}
	prev := dummyHead
	for head != nil {
		if head.Next != nil && head.Val == head.Next.Val {
			for head.Next != nil && head.Val == head.Next.Val {
				head = head.Next
			}

			prev.Next = head.Next
		} else {
			prev = prev.Next
		}

		head = head.Next
	}

	return dummyHead.Next
}
