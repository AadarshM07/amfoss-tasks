package main

import (
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	// Read the input 
	data, _ := ioutil.ReadFile("input.txt")
	input := strings.TrimSpace(string(data))
	n, _ := strconv.Atoi(input)

	var output strings.Builder

	// Upper half of the diamond
	for i := 1; i <= n; i += 2 {
		output.WriteString(strings.Repeat(" ", (n-i)/2))
		output.WriteString(strings.Repeat("*", i))  
		output.WriteString("\n")                         
	}

	// Lower half of the diamond
	for i := n - 2; i > 0; i -= 2 {
		output.WriteString(strings.Repeat(" ", (n-i)/2)) 
		output.WriteString(strings.Repeat("*", i))       
		output.WriteString("\n")                         
	}

	// Write the output to "output.txt"
	ioutil.WriteFile("output.txt", []byte(output.String()), 0644)
}
