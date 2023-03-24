package main

import (
	"GinProject/src/Model"
	"GinProject/src/Routers"
	"fmt"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.Use(cors.Default())
	Routers.UserRouterInit(r)
	RecommendList := Model.RecommendRecord{}
	Model.DB.First(&RecommendList)
	fmt.Println(RecommendList)
	r.Run(":8087")
}
