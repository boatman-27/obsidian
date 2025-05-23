---
tags:
  - go
date: 2025-03-20T00:22:00
---
```env
PG_USER="postgres"
PG_PASSWORD="Ao260221_@"
PG_HOST="localhost"
PG_DATABASE="Maths"
PG_PORT="5432"
```

```sh
go get github.com/joho/godotenv   
go get -u github.com/lib/pq
go get github.com/jmoiron/sqlx

```

```go
package db

import (
	"database/sql"
	"fmt"
	"log"
	"os"
	"github.com/joho/godotenv"
	_ "github.com/lib/pq"
)

  

var DB *sql.DB

  

func ConnectDB() {
	err := godotenv.Load()
	if err != nil {
		log.Fatalf("Error loading .env file")
	}

	psqlInfo := fmt.Sprintf(
		"host=%s port=%s user=%s password=%s dbname=%s sslmode=disable",
		os.Getenv("PG_HOST"), os.Getenv("PG_PORT"),
		os.Getenv("PG_USER"), os.Getenv("PG_PASSWORD"),
		os.Getenv("PG_DATABASE"),
	)
	fmt.Println(os.Getenv("PG_DATABASE"))
	
	// Connect to PostgreSQL
	db, err := sql.Open("postgres", psqlInfo)
	if err != nil {
		log.Fatalf("Error opening DB connection: %v", err)
	}
	
	// Check connection
	err = db.Ping()
	if err != nil {
		log.Fatalf("Error connecting to the database: %v", err)
	}
	fmt.Println("Successfully connected to PostgreSQL")
	DB = db
}
```

OR

```go
package db

import (
	"log"
	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"

)

var DB *sqlx.DB

func ConnectDB() {
	var err error
	DB, err = sqlx.Open("postgres", "user=postgres password=Ao260221_@ dbname=Maths sslmode=disable")	
	if err != nil {
		log.Fatal(err)
	}
}
```