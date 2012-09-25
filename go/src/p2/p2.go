package main

import "fmt"

func main() {
	s, p, q := 0, 1, 2
	for p < 4000000 {
		if p % 2 == 0 {
			s += p
		}
		p, q = q, p+q
	}
	fmt.Println(s)
}