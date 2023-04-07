package Controller

import (
	"GinProject/src/API"
	"GinProject/src/Model"
	"GinProject/src/Util"
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
	"strconv"
	"strings"
	"time"
)

type UserController struct {
}

func (con UserController) Register(context *gin.Context) {
	json := make(map[string]interface{})
	context.BindJSON(&json)
	Nickname := fmt.Sprintf("%s", json["nickname"])
	sex, _ := strconv.Atoi(fmt.Sprintf("%s", json["sex"]))
	Birthday := fmt.Sprintf("%s", json["birthday"])
	tmp := strings.Split(Birthday, "-")
	BirthdayYear, _ := strconv.Atoi(tmp[0])
	BirthdayMonth, _ := strconv.Atoi(tmp[1])
	BirthdayDate, _ := strconv.Atoi(tmp[2][:2])
	personalSignature := fmt.Sprintf("%s", json["personal_signature"])
	email := fmt.Sprintf("%s", json["email"])
	password := fmt.Sprintf("%s", json["password"])
	ret := API.UserAPI{}.Insert(Model.User{
		Nickname:          Nickname,
		Password:          password,
		Birthday:          time.Date(BirthdayYear, time.Month(BirthdayMonth), BirthdayDate, 0, 0, 0, 0, time.UTC),
		Sex:               sex,
		PersonalSignature: personalSignature,
		Email:             email,
	})
	if ret == false {
		context.JSON(http.StatusOK, gin.H{
			"response": false,
		})
	} else {
		context.JSON(http.StatusOK, gin.H{
			"response": true,
		})
	}
}

func (con UserController) GetRecommend(context *gin.Context) {
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

func (con UserController) ReceiveComment(context *gin.Context) {
	json := make(map[string]interface{})
	context.BindJSON(&json)
	belongMovieId, _ := strconv.Atoi(fmt.Sprint(json["belong_movie_id"]))
	userId, _ := strconv.Atoi(fmt.Sprint(json["user_id"]))
	comment := fmt.Sprint(json["comment"])
	ret := API.CommentAPI{}.Insert(comment, userId, belongMovieId)
	if ret {
		context.JSON(http.StatusOK, gin.H{"response": true})
	} else {
		context.JSON(http.StatusOK, gin.H{
			"state": false,
		})
	}
}

func (con UserController) SelectComment(context *gin.Context) {
	json := make(map[string]interface{})
	context.BindJSON(&json)
	belongMovieId, _ := strconv.Atoi(fmt.Sprint(json["belong_movie_id"]))
	fmt.Println(belongMovieId)
	ret := API.CommentAPI{}.FindAllCommentOfOneMovie(belongMovieId)
	context.JSON(http.StatusOK, gin.H{
		"response": true,
		"content":  ret,
	})
}

func (con UserController) Login(context *gin.Context) {
	json := make(map[string]interface{})
	context.BindJSON(&json)
	email := fmt.Sprintf("%s", json["email"])
	password := fmt.Sprintf("%s", json["password"])
	ret := API.UserAPI{}.CheckLogin(email, password)
	if len(ret) == 1 {
		token, _ := Util.ReleaseToken(fmt.Sprintf("%d", ret[0].UserId), email, password)
		context.JSON(http.StatusOK, gin.H{
			"response": true,
			"token":    token,
		})
	} else {
		context.JSON(http.StatusOK, gin.H{
			"response": false,
		})
	}
}

func (con UserController) CheckToken(ctx *gin.Context) {
	json := make(map[string]interface{})
	ctx.BindJSON(&json)
	token := fmt.Sprintf("%s", json["token"])
	_, claim, _ := Util.ParseToken(token)
	UserId, _ := strconv.Atoi(claim.UserId)
	ret := API.UserAPI{}.GetInfo(UserId)
	if len(ret) != 1 {
		ctx.JSON(http.StatusOK, gin.H{
			"response": false,
		})
	} else {
		fmt.Println("okokok")
		ctx.JSON(http.StatusOK, gin.H{
			"response": true,
			"user_id":  ret[0].UserId,
			"nickname": ret[0].Nickname,
			"password": ret[0].Password,
			"sex":      ret[0].Sex,
			"birthday": ret[0].Birthday,
			"email":    ret[0].Email,
		})
	}
}
