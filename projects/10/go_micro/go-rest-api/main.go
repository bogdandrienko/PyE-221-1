package main

import (
	"database/sql"
	"errors"
	"fmt"
	"github.com/gin-gonic/gin"
	_ "github.com/lib/pq"
	"log"
	"net/http"
	"os"
	"reflect"
	"time"
)

func a1Variables() {
	// write code
	// build code (to binary/main.exe)
	// run binary file

	fmt.Println("Hello world!")       // Hello world!
	fmt.Println(reflect.TypeOf("Go")) // string

	// todo dynamic typing (Python / JavaScript / PHP)
	// name = "Python"
	// name = 12

	// todo python static-like typing
	// name: str = "Python"

	// todo static typing (Go / C++ / C#)
	var name string = "Golang"
	name = "123123"
	fmt.Println(name)

	// 1 - pre init
	var bool1 bool
	bool1 = true
	fmt.Println(bool1)

	// 2 - init
	var bool2 bool = true
	fmt.Println(bool2)

	// 3 - short init
	bool3 := true
	fmt.Println(bool3)
}

func a2TypeVariables() {
	// bool
	bool1 := true
	fmt.Println(bool1)

	// string
	string1 := "Golang"
	fmt.Println(string1)

	// rune
	rune1 := 'P'
	fmt.Println(rune1)

	// numbers negative + positive
	var int1 int = 12 // int32
	fmt.Println(int1)

	var int2 int8 = 12 // 4 bytes * 1 000 000 = 4 mb |
	fmt.Println(int2)

	var int3 int16 = 12 // 16 bytes * 1 000 000 = 16 mb |
	fmt.Println(int3)

	var int4 int32 = 12 // 256 bytes * 1 000 000 = 4 mb |
	fmt.Println(int4)   //

	var int5 int64 = 12 // 1024 bytes * 1 000 000 = 4 mb |
	fmt.Println(int5)

	// numbers only positive
	var uint1 uint = 12 // int32
	fmt.Println(uint1)

	var uint2 uint8 = 12 // 4 bytes * 1 000 000 = 4 mb |
	fmt.Println(uint2)

	var uint3 uint16 = 12 // 16 bytes * 1 000 000 = 16 mb |
	fmt.Println(uint3)

	var uint4 uint32 = 12 // 256 bytes * 1 000 000 = 4 mb |
	fmt.Println(uint4)    //

	var uint5 int64 = 12 // 1024 bytes * 1 000 000 = 4 mb |
	fmt.Println(uint5)

	// numbers with float point
	var float1 float32 = 12.0
	fmt.Println(float1)

	var float2 float64 = 12.0
	fmt.Println(float2)

	float3 := 12.0
	fmt.Println(float3)

	// arrays (!not a list on Python)
	var arr1 [3]int = [3]int{1, 2, 3}
	fmt.Println(arr1)

	var arr2 [5]bool = [5]bool{}
	fmt.Println(arr2)

	var arr3 = [...]int{1, 2, 3}
	fmt.Println(arr3)

	// slice (python-like "list")
	var slice1 []int = []int{1, 2, 3}
	fmt.Println(slice1)

	var slice2 []int = []int{}
	fmt.Println(slice2)

	slice3 := []string{"Slice1", "11"}
	fmt.Println(slice3)

	slice4 := make([]int, 5) // 5 - capacity
	fmt.Println(slice4)

	// ёмкость - любой массив всегда имеет ограниченную длину,
	// когда мы добавляем в срез новый элемент, он "пересобирается"
	// компилятор собирает новый массив, в 2 раза больше старого
	// 10 20 40 80 160 320 640 1280

	// map (dict python)
	//var map1 = make(map[string]string)
	// var map2 = make(map[any]any)
	var map3 = make(map[string]any)
	fmt.Println(map3)
	map3["name"] = "Alice"
	map3["age"] = 25
	fmt.Println(map3)
	fmt.Println(map3["age"])
	delete(map3, "age")
	fmt.Println(map3)
}

func a3Structs() {
	// structs (python like class)
	var user1 struct {
		name string
		age  int
	}
	fmt.Printf("%+v\n", user1)

	user2 := struct {
		name string
		age  int
		sex  bool
	}{"Vasya", 25, true}
	fmt.Printf("%+v\n", user2)

}

func a4Operators() {
	var1 := 12
	var1++
	var1--

	var1 += 1
	var1 -= 1
	var1 *= 1
	var1 /= 1
	var1 %= 1

	var2 := false
	var2 = 12 == 1
	var2 = 12 != 1

	var2 = 12 > 1
	var2 = 12 < 1
	var2 = 12 >= 1
	var2 = 12 <= 1

	fmt.Println(var2)
}

func a5Conditions() {
	age := 25

	// if
	if age > 18 {
		fmt.Println("Вы соврешеннолетний!")
	}

	// if + else
	if age > 18 {
		fmt.Println("Вы соврешеннолетний!")
	} else {
		fmt.Println("Вы не соврешеннолетний!")
	}

	// if + else if
	if age > 18 {
		fmt.Println("Вы соврешеннолетний!")
	} else if age > 18 {
		fmt.Println("Вы соврешеннолетний!")
	} else {
		fmt.Println("Вы не соврешеннолетний!")
	}

	fruit := "Banana"

	// switch
	switch fruit {
	case "Kiwi":
		{
			fmt.Println("I'm a kiwi")
		}
	case "Banana":
		fmt.Println("I'm a banana")
	default:
		fmt.Println("I'm a unknown")
	}
}

func checkAdult(age int) (bool, error) {
	if age < 0 {
		return false, errors.New("Возраст не соответствует валидным значениям")
	}

	if age > 17 {
		return true, nil
	}
	return false, nil
}

func a6Errors() {
	result, err := checkAdult(24)
	if err != nil { // python like EXCEPTION
		fmt.Printf("!ERROR!: %s", err)
		return
	} else {
		fmt.Println(result)
	}
}

func a7Loops() {
	slice1 := []string{"Python", "Go", "C++"} //
	elem1 := "Go"
	for i := 0; i < len(slice1); i += 1 {
		if slice1[i] == elem1 {
			fmt.Println("FIND")
		}
	}

	for i := 1; i <= 10000; i += 1 {
		for j := 1; j <= 10000; j += 1 {
			fmt.Println(j, i)
		}
	}

	// O(!n)
	// O(2^n)
	// O(n2)
	// O(n) 0.001s * 1 000 000 (N) = for i 1 000 000 = 999 999 = 999 998 = 999 997 = 999 996
	// O(log(n)) 0.001s * 1 000 000 (N) = 500 000 = 250 000 = 125 000 = 75 000
	// O(1) - map(dict)

	// classic loop
	for i := 0; i < len(slice1); i += 1 {
		//fmt.Println(i)         // index
		//fmt.Println(slice1[i]) // elem
	}

	// foreach loop
	for _, value := range slice1 {
		//fmt.Println(index) // index
		fmt.Println(value) // elem
	}
}

func MiddlewareLogger(next gin.HandlerFunc) gin.HandlerFunc {
	return func(request *gin.Context) {
		// todo

		fmt.Println("I'm a logger:", time.Now(), request.Request.Method, request.Request.RequestURI)
		// todo

		next(request)
	}
}

func MiddlewareAuth(next gin.HandlerFunc) gin.HandlerFunc {
	return func(request *gin.Context) {
		// todo
		fmt.Println(request.Request.Header.Get("Authorization"))
		// todo

		next(request)
	}
}

func connectToDb() ([]string, error) {
	source := fmt.Sprintf(
		"host=%s port=%d user=%s password=%s dbname=%s sslmode=%s",
		"127.0.0.1", 5432, "gin_usr", "12345Qwerty!", "gin_db", "disable",
	)
	dbConnection, err := sql.Open("postgres", source)
	if err != nil {
		// return errors.New("Database error")
		return nil, err
	}
	defer dbConnection.Close() // after all
	rows, err := dbConnection.Query("select title from books;")
	if err != nil {
		return nil, err
	}

	titles := make([]string, 0)
	for rows.Next() {
		var title string
		err = rows.Scan(&title)
		if err != nil {
			return nil, err
		}
		titles = append(titles, title)
	}
	fmt.Println(titles)

	err = rows.Err()
	if err != nil {
		return nil, err
	}

	return titles, nil
}

func helloWorld(c *gin.Context) {
	data := map[string]any{"name": "Bogdan", "age": 666}

	titles, err := connectToDb()
	if err != nil {
		log.Fatal(err)
	}
	data["1"] = titles[0]
	data["2"] = titles[1]
	data["3"] = titles[2]

	c.JSON(http.StatusOK, data) // dictionary
	// ассоциативный массив
}

type Data struct {
	Text   string `json:"text"`
	Count  int32  `json:"count"`
	IsHide bool   `json:"is_hide"` // !CAPITAL
}

func postLogger(c *gin.Context) {
	name := "new"
	//file, err := os.OpenFile(fmt.Sprintf("%s_log.txt", name), os.O_RDWR|os.O_CREATE, 0644)
	file, err := os.OpenFile(fmt.Sprintf("%s_log.txt", name), os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	defer file.Close()
	if err != nil {
		c.JSON(http.StatusBadRequest, map[string]any{"error": err.Error()})
		return
	}

	var data Data
	if err := c.BindJSON(&data); err != nil {
		c.JSON(http.StatusBadRequest, map[string]any{"error": err.Error()})
		return
	}
	if len(data.Text) < 1 {
		c.JSON(http.StatusBadRequest, map[string]any{"error": errors.New("no data").Error()})
		return
	}
	text := ""
	if data.IsHide == true {
		text = "Забанен"
	} else {
		text = "Не забанен"
	}
	_, err = file.WriteString(data.Text + fmt.Sprintf("[%d] (%s)", data.Count, text) + "\n")
	if err != nil {
		c.JSON(http.StatusBadRequest, map[string]any{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, map[string]any{"response": "Success"})
}

func ginRun() {
	gin.SetMode(gin.DebugMode)
	var r = gin.New()

	// router - маршрутизация
	r.GET("/", MiddlewareLogger(MiddlewareAuth(helloWorld)))
	r.GET("/home", MiddlewareLogger(MiddlewareAuth(helloWorld)))        // curl -v -X GET 127.0.0.1:8000/home
	r.POST("/api/logger", MiddlewareLogger(MiddlewareAuth(postLogger))) // curl -v -X POST 127.0.0.1:8000/api/logger -d '{"text":"Hello Go", "count": 12, "is_hide": true}'
	//r.PUT()
	//r.DELETE()

	err := r.Run(fmt.Sprintf("%s:%d", "127.0.0.1", 8000))
	if err != nil {
		log.Fatal(err)
		return
	}
}

func main() {
	//a1Variables()
	//a2TypeVariables()
	//a3Structs()
	//a4Operators()
	//a5Conditions()
	//a6Errors()
	//a7Loops()

	// https://habr.com/ru/post/188010/
	ginRun()
	//err := postLogger("hello world")
	//if err != nil {
	//	log.Fatal(err)
	//	return
	//}

}
