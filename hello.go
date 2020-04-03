package main

import (
	"net/http"

	"github.com/gorilla/mux" // Your imported package
)

func yourHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Gorilla!\n"))
}

func main() {
	r := mux.NewRouter()
	// Routes consist of a path and a handler function.
	r.HandleFunc("/", yourHandler)

	// Bind to a port and pass our router in
	panic(http.ListenAndServe(":8000", r))
}
