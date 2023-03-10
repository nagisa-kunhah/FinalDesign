package Model

import (
	"fmt"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

var DB *gorm.DB
var err error

func init() {
	fmt.Println("init core.....")
	dsn := "root:root@tcp(127.0.0.1:3306)/test?charset=utf8mb4&parseTime=True&loc=Local"
	DB, err = gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		fmt.Println("link mysql error!!!!!!!!!!!!!", err)
	}
	if DB == nil {
		fmt.Println("????????????????")
	}
	fmt.Println("ok init core!!!")
	RecommendList := RecommendRecord{}
	DB.First(&RecommendList)
}
