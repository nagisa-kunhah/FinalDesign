package API

import (
	"GinProject/src/Model"
	"fmt"
)

type UserAPI struct {
}

func (api UserAPI) Insert(data Model.User) bool {
	err := Model.DB.Debug().Create(data).Error
	if err != nil {
		return false
	}
	return true
}

func (api UserAPI) CheckLogin(email string, password string) []Model.User {
	var result []Model.User
	Model.DB.Debug().Where("email=? AND password=?", email, password).Find(&result)
	fmt.Println(result)
	return result
}

func (api UserAPI) GetInfo(UserId int) []Model.User {
	var result []Model.User
	Model.DB.Where("user_id=?", UserId).Find(&result)
	fmt.Println(result)
	return result
}
