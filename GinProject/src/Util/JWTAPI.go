package Util

import (
	"fmt"
	"github.com/golang-jwt/jwt/v4"
	"time"
)

var jwtKey = "akexc-jwt-4396"

func ReleaseToken(UserId, Email, PassWord string) (string, error) {
	expirationTime := jwt.NewNumericDate(time.Now().Add(24 * time.Hour))
	claim := Claim{
		UserId:   UserId,
		Email:    Email,
		Password: PassWord,
		RegisteredClaims: jwt.RegisteredClaims{
			ExpiresAt: expirationTime,
			NotBefore: jwt.NewNumericDate(time.Now()),
			IssuedAt:  jwt.NewNumericDate(time.Now()),
			Issuer:    "admin",
			Subject:   "user_id",
			Audience:  jwt.ClaimStrings{},
			ID:        "id",
		},
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claim)
	fmt.Println(token)
	tokenString, err := token.SignedString([]byte(jwtKey))
	if err != nil {
		return "", err
	}
	return tokenString, nil
}

func ParseToken(tokenString string) (*jwt.Token, *Claim, error) {
	claims := &Claim{}
	token, err := jwt.ParseWithClaims(tokenString, claims, func(token *jwt.Token) (interface{}, error) {
		return []byte(jwtKey), nil
	})
	if err != nil {
		fmt.Println("????????????????????")
	}
	return token, claims, err
}
