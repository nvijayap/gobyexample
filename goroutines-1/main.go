package main

import (
	"fmt"
	"time"
)

func main() {

	go func(msg string) {
		fmt.Println(msg)
	}("goroutine")

	// allows above goroutine to complete before exiting program
	time.Sleep(time.Millisecond)
}
