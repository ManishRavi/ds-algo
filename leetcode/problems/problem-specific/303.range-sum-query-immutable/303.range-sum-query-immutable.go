package main

type NumArray struct {
	Nums  []int
	Cache []int
}

func Constructor(nums []int) NumArray {
	obj := NumArray{nums, make([]int, len(nums)+1)}
	for i := range obj.Nums {
		obj.Cache[i+1] = obj.Cache[i] + obj.Nums[i]
	}

	return obj
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.Cache[right+1] - this.Cache[left]
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(left,right);
 */
