/*
 * @lc app=leetcode id=155 lang=golang
 *
 * [155] Min Stack
 */

// @lc code=start
type MinStack struct {
	RealStack []int
	MinStack  []int
}

func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(val int) {
	this.RealStack = append(this.RealStack, val)
	if len(this.MinStack) <= 0 || val <= this.MinStack[len(this.MinStack)-1] {
		this.MinStack = append(this.MinStack, val)
	}
}

func (this *MinStack) Pop() {
	val := this.RealStack[len(this.RealStack)-1]
	this.RealStack = this.RealStack[:len(this.RealStack)-1]
	if val == this.MinStack[len(this.MinStack)-1] {
		this.MinStack = this.MinStack[:len(this.MinStack)-1]
	}
}

func (this *MinStack) Top() int {
	return this.RealStack[len(this.RealStack)-1]
}

func (this *MinStack) GetMin() int {
	return this.MinStack[len(this.MinStack)-1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
// @lc code=end

