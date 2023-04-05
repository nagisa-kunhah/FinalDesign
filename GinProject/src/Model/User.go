package Model

import "time"

type User struct {
	UserId            int
	Nickname          string
	Password          string
	Sex               int
	Birthday          time.Time
	PersonalSignature string
	Email             string
}

func (User) TableName() string {
	return "user"
}
