package Test

import (
	"GinProject/src/API"
	"GinProject/src/Model"
	"fmt"
	"testing"
	"time"
)

func TestUserAPIInsert(t *testing.T) {
	Birthday := time.Date(2000, time.Month(6), 26, 0, 0, 0, 0, time.UTC)
	ret := API.UserAPI{}.Insert(Model.User{
		Nickname:          fmt.Sprintf("%s", "nagisa"),
		Birthday:          Birthday,
		Sex:               1,
		PersonalSignature: "aaaaaaaa",
		Email:             "1434936049@qq.com",
	})
	fmt.Println(ret)
}
func TestUserAPICheckLogin(t *testing.T) {

}
