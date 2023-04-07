package Model

import "time"

type CommentRecord struct {
	CommentId     int
	BelongMovieId int
	UserId        int
	Comment       string
	CommitTime    time.Time
	UpVote        int
	DownVote      int
}

func (CommentRecord) TableName() string {
	return "comments"
}
