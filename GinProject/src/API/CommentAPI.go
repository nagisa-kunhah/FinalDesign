package API

import (
	"GinProject/src/Model"
	"time"
)

type CommentAPI struct {
}

func (api CommentAPI) Insert(comment string, userId int, belongMovieId int) bool {
	err := Model.DB.Debug().Create(Model.CommentRecord{
		BelongMovieId: belongMovieId,
		UserId:        userId,
		Comment:       comment,
		CommitTime:    time.Now(),
		UpVote:        0,
		DownVote:      0,
	}).Error
	if err != nil {
		return false
	}
	return true
}

func (api CommentAPI) FindAllCommentOfOneMovie(movieId int) []Model.CommentRecord {
	var result []Model.CommentRecord
	Model.DB.Debug().Where("belong_movie_id = ?", movieId).Order("commit_time DESC").Find(&result)
	return result
}
