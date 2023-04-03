package main

import (
	"GinProject/src/Routers"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.Use(cors.Default())
	Routers.UserRouterInit(r)
	r.Run(":8087")
}
