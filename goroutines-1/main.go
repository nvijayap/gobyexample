package main

import (
	"fmt"
	"time"
)

func main() {

	go func(msg string) {
		fmt.Println(msg)
	}("goroutine")

	time.Sleep(time.Millisecond)
}
