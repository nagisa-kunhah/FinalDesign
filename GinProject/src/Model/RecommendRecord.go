package Model

type RecommendRecord struct {
	UserId  int
	MovieId string
}

func (RecommendRecord) TableName() string {
	return "recommend"
}
