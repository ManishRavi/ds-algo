/*
 * @lc app=leetcode id=23 lang=golang
 *
 * [23] Merge k Sorted Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// * Divide and Conquer Solution | O(nlog(k)) Time | O(1) Space

func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) <= 0 {
		return nil
	}

	interval := 1
	for interval < len(lists) {
		for i := 0; i+interval < len(lists); i = i + (interval * 2) {
			lists[i] = mergeLists(lists[i], lists[i+interval])
		}

		interval *= 2
	}

	return lists[0]
}

func mergeLists(list1, list2 *ListNode) *ListNode {
	dummyHead := &ListNode{0, nil}
	cur := dummyHead
	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			cur.Next = list1
			list1 = list1.Next
		} else {
			cur.Next = list2
			list2 = list2.Next
		}

		cur = cur.Next
	}

	if list1 != nil {
		cur.Next = list1
	} else {
		cur.Next = list2
	}

	return dummyHead.Next
}

// @lc code=end

