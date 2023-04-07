package Test

import (
	"GinProject/src/API"
	"fmt"
	"testing"
)

func Test1(t *testing.T) {
	ret := API.CommentAPI{}.Insert("aaa", 1, 1)
	if ret != true {
		t.Error("fail 1")
		t.Failed()
	}
	ret = API.CommentAPI{}.Insert("aaa", 0, 1)
	if ret == true {
		t.Error("fail 2")
		t.Failed()
	}
	ret = API.CommentAPI{}.Insert("aaa", 1, 0)
	if ret == true {
		t.Error("fail 3")
		t.Failed()
	}
	ret = API.CommentAPI{}.Insert("aaa", 1, 2)
	if ret != true {
		t.Error("fail 4")
		t.Failed()
	}
	ret = API.CommentAPI{}.Insert("aaa", 1, 3)
	if ret != true {
		t.Error("fail 5")
		t.Failed()
	}
}

func Test2(t *testing.T) {
	ret := API.CommentAPI{}.FindAllCommentOfOneMovie(1)
	fmt.Println(ret)
}
