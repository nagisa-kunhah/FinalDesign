package Controller

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

type TestController struct {
}

func (con TestController) SetCookie(c *gin.Context) {
	fmt.Println("ohhhhhhhhhhhhhhhhh")
	c.SetCookie("user_name", "nagisa", 3600*24, "/", "http://localhost:8087", false, true)
	c.JSON(http.StatusOK, gin.H{
		"response": true,
	})
}

func (con TestController) GetCookie(c *gin.Context) {
	cookie, err := c.Cookie("user_name")
	if err != nil {
		c.JSON(http.StatusOK, gin.H{
			"response": false,
		})
	}
	fmt.Printf("Cookie value: %s \n", cookie)
	c.JSON(http.StatusOK, gin.H{
		"response": true,
		"cookie":   cookie,
	})
}
