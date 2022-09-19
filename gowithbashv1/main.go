package main

import (
	"log"
	"os"
	"github.com/logocomune/maclookup-go"
)

func main() {
        macAddressToLookup := os.Args[1]
	client := maclookup.New()
    
	r, err := client.CompanyName(macAddressToLookup)

	if err != nil {
		log.Fatal(err)
	}
	log.Println("MAC found in database:", r.Found)
	log.Println("MAC is private (no company name):", r.IsPrivate)
	log.Println("Company name:", r.Company)
	log.Println("Api response in: ", r.RespTime)
	log.Println("Rate limits - remaining request for current time window:", 
r.RateLimit.Remaining)
	log.Println("Rate limits - next reset", r.RateLimit.Reset)

}

