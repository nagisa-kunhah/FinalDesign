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
	json := make(map[string]interface{})
	context.BindJSON(&json)
	userId := json["id"]
	var records []Model.RecommendRecord
	fmt.Println(userId)
	Model.DB.Where("user_id = ?", userId).Find(&records)
	var movies []string = make([]string, 0)
	for _, item := range records {
		movies = append(movies, item.MovieId)
	}
	fmt.Println("ok collect")
	var movieRecord []Model.MovieRecord
	Model.DB.Where("movieId in ?", movies).Find(&movieRecord)
	//fmt.Println(movieRecord[0].Title)
	var recommendTitle = make([]string, 0)
	for i := 0; i < len(movieRecord); i++ {
		recommendTitle = append(recommendTitle, movieRecord[i].Title)
	}
	context.JSON(http.StatusOK, gin.H{"recommend": movies, "recommend_title": recommendTitle})
}
