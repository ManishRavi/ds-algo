package main

func hammingDistance(x int, y int) int {
	count := 0
	for i := 0; i < 32; i++ {
		count += (x & 1) ^ (y & 1)
		x >>= 1
		y >>= 1
	}

	return count
}
