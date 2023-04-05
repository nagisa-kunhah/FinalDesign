package Controller

import (
	"GinProject/src/API"
	"GinProject/src/Model"
	"fmt"
	"github.com/gin-gonic/gin"
	"math/rand"
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
	fmt.Println("work......")
	json := make(map[string]interface{})
	context.BindJSON(&json)
	userId := json["id"]
	var records []Model.RecommendRecord
	fmt.Println(userId)
	Model.DB.Where("user_id = ?", userId).Find(&records)
	var movies []string = make([]string, 0)
	for _, item := range records {
		fmt.Println(item)
		id := strconv.Itoa(rand.Intn(30) + 1)
		movies = append(movies, id)
		fmt.Println(id)
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
	userId, _ := strconv.Atoi(fmt.Sprintf("%s", json["userId"]))
	comment := fmt.Sprintf("%s", json["Comment"])
	fmt.Println("userId:", json["userId"])
	fmt.Println("Comment:", json["Comment"])
	commitTime := time.Now()
	record := Model.CommentRecord{
		UserId:     userId,
		Comment:    comment,
		CommitTime: commitTime,
	}
	Model.DB.Debug().Create(record)
	//fmt.Println("ok insert")
	context.JSON(http.StatusOK, gin.H{"statue": "ok"})
}

func (con UserController) Login(context *gin.Context) {
	json := make(map[string]interface{})
	context.BindJSON(&json)
	email := fmt.Sprintf("%s", json["email"])
	password := fmt.Sprintf("%s", json["password"])
	ret := API.UserAPI{}.CheckLogin(email, password)
	if ret == true {
		context.JSON(http.StatusOK, gin.H{
			"response": true,
		})
	} else {
		context.JSON(http.StatusOK, gin.H{
			"response": false,
		})
	}
}
