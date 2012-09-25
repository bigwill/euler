package main

import "fmt"

func PrimeFactors(n int64, c chan int64) {
	var p int64
	p = 2
	for n > 1 {
		if n % p == 0 {
			c <- p
			n /= p
		} else {
			p++
		}
	}
	c <- 0
}

func main() {
	c := make(chan int64)
	go PrimeFactors(600851475143, c)
	var lpf, f int64
	lpf, f = 0, 1
	for f != 0 {
		f = <- c
		if f > 0 {
			lpf = f
		}
	}
	fmt.Println(lpf)
}