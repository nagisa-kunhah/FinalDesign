package main

import (
	"GinProject/src/Model"
	"GinProject/src/Routers"
	"fmt"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	Routers.UserRouterInit(r)
	RecommendList := Model.RecommendRecord{}
	Model.DB.First(&RecommendList)
	fmt.Println(RecommendList)
	r.Run() // 监听并在 0.0.0.0:8080 上启动服务
}
