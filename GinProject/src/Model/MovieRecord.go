package Model

type MovieRecord struct {
	MovieId int
	Title   string
	Genres  string
}

func (MovieRecord) TableName() string {
	return "movies"
}
