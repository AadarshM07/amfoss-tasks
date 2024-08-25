//subtask2 AM@FOSS
package main

import (
	"io/ioutil"
)

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err == nil {
		ioutil.WriteFile("output.txt", data, 0644)
	}
	
}
