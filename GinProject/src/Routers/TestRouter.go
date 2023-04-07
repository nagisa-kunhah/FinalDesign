package Routers

import (
	"GinProject/src/Controller"
	"github.com/gin-gonic/gin"
)

func TestRouterInit(r *gin.Engine) {
	TestRouter := r.Group("/test")
	{
		TestRouter.GET("/set_cookie", Controller.TestController{}.SetCookie)
		TestRouter.GET("/get_cookie", Controller.TestController{}.GetCookie)
	}
}
