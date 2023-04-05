package Model

import "time"

type CommentRecord struct {
	CommentId  int
	UserId     int
	Comment    string
	CommitTime time.Time
}

func (CommentRecord) TableName() string {
	return "comments"
}
