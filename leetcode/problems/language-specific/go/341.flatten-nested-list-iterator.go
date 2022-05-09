/*
 * @lc app=leetcode id=341 lang=golang
 *
 * [341] Flatten Nested List Iterator
 */

// @lc code=start
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (this NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (this NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (this *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (this NestedInteger) GetList() []*NestedInteger {}
 */

// * Recursive Solution | O(n) Time | O(n) Space

type NestedIterator struct {
	FlattenedList []int
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
	flattenedList := []int{}
	flattenList(nestedList, &flattenedList)
	return &NestedIterator{flattenedList}
}

func (this *NestedIterator) Next() int {
	nextVal := this.FlattenedList[0]
	this.FlattenedList = this.FlattenedList[1:]
	return nextVal
}

func (this *NestedIterator) HasNext() bool {
	return len(this.FlattenedList) > 0
}

func flattenList(nestedList []*NestedInteger, flattenedList *[]int) {
	for _, v := range nestedList {
		// * If the value is an integer then add it to the flattened list
		if v.IsInteger() {
			*flattenedList = append(*flattenedList, v.GetInteger())
		} else {
			// * If the value is a nested list do a recursive call
			flattenList(v.GetList(), flattenedList)
		}
	}
}

// @lc code=end

