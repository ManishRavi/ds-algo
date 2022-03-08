package main

func maxProfit(prices []int) int {
	if len(prices) <= 1 {
		return 0
	}

	left, maxProfit := 0, 0
	for right := 1; right < len(prices); right++ {
		if prices[right] > prices[left] {
			maxProfit = findMax(maxProfit, prices[right]-prices[left])
		} else {
			left = right
		}
	}

	return maxProfit
}

func findMax(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
