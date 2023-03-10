package Controller

import (
	"GinProject/src/Model"
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

type UserController struct {
}

func (con UserController) GetRecommend(context *gin.Context) {
	fmt.Println("work......")
	var records []Model.RecommendRecord
	Model.DB.Where("user_id = ?", "1").Find(&records)
	var movies []string = make([]string, 0)
	for _, item := range records {
		movies = append(movies, item.MovieId)
	}
	fmt.Println("ok collect")
	context.JSON(http.StatusOK, gin.H{"recommend": movies})
}
