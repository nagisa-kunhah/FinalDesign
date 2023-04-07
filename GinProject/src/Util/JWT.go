package Util

import "github.com/golang-jwt/jwt/v4"

type Claim struct {
	UserId           string `json:"user_id"`
	Email            string `json:"email"`
	Password         string `json:"password"`
	RegisteredClaims jwt.RegisteredClaims
}

func (c Claim) Valid() error {
	return nil
}
