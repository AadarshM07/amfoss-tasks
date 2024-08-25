package main

import "fmt"

func main() {
	var n int
	fmt.Print("Enter a number: ")
	fmt.Scan(&n)

	// Upper half of the diamond
	for i := 1; i <= n; i += 2 {
		for j := 0; j < (n-i)/2; j++ {
			fmt.Print(" ")
		}
		for k := 0; k < i; k++ {
			fmt.Print("*")
		}
		fmt.Println()
	}

	for i := n - 2; i > 0; i -= 2 {
		for j := 0; j < (n-i)/2; j++ {
			fmt.Print(" ")
		}
		for k := 0; k < i; k++ {
			fmt.Print("*")
		}
		fmt.Println()
	}
}
