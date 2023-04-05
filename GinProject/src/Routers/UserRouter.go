package Routers

import (
	"GinProject/src/Controller"
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

func UserRouterInit(r *gin.Engine) {
	UserRouter := r.Group("/user")
	{
		UserRouter.GET("/index", Controller.UserController{}.GetRecommend)
		UserRouter.GET("/test", func(context *gin.Context) {
			context.JSON(http.StatusOK, gin.H{
				"test": 1,
			})
		})
		UserRouter.POST("/test_input", func(context *gin.Context) {
			for k := range context.Request.URL.Query() {
				fmt.Println(k, " ", context.Query(k))
			}
			json := make(map[string]interface{})
			context.BindJSON(&json)
			fmt.Println(json)
			id := json["id"]
			context.JSON(http.StatusOK, gin.H{
				"id": id,
			})
		})
		UserRouter.POST("/get_recommend", Controller.UserController{}.GetRecommend)
		UserRouter.POST("/sent_comment", Controller.UserController{}.ReceiveComment)
		UserRouter.POST("/Register", Controller.UserController{}.Register)
		UserRouter.POST("/Login", Controller.UserController{}.Login)
	}
}
