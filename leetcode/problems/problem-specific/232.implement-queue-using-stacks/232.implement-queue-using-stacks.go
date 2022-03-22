package main

type MyQueue struct {
	PushStack []int
	PopStack  []int
}

func Constructor() MyQueue {
	return MyQueue{}
}

func (this *MyQueue) Push(x int) {
	this.PushStack = append(this.PushStack, x)
}

func (this *MyQueue) Pop() int {
	this.shiftStacks()
	el := this.PopStack[len(this.PopStack)-1]
	this.PopStack = this.PopStack[:len(this.PopStack)-1]
	return el
}

func (this *MyQueue) Peek() int {
	this.shiftStacks()
	return this.PopStack[len(this.PopStack)-1]
}

func (this *MyQueue) Empty() bool {
	return len(this.PopStack) <= 0 && len(this.PushStack) <= 0
}

func (this *MyQueue) shiftStacks() {
	if len(this.PopStack) <= 0 {
		for len(this.PushStack) > 0 {
			this.PopStack = append(this.PopStack, this.PushStack[len(this.PushStack)-1])
			this.PushStack = this.PushStack[:len(this.PushStack)-1]
		}
	}
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
