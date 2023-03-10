package Routers

import (
	"GinProject/src/Controller"
	"github.com/gin-gonic/gin"
)

func UserRouterInit(r *gin.Engine) {
	UserRouter := r.Group("/user")
	{
		UserRouter.GET("/index", Controller.UserController{}.GetRecommend)
	}
}
