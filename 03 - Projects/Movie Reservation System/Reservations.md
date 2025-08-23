## sql table
```sQL
CREATE TABLE reservations (
    reservationid    VARCHAR(10) PRIMARY KEY,
    userid           TEXT NOT NULL REFERENCES users(userid),
    showtimeid       TEXT NOT NULL REFERENCES showtimes(showtimeid),
    numberofseats    INT NOT NULL CHECK (numberofseats > 0),
    totalprice       NUMERIC(10, 2) NOT NULL CHECK (totalprice >= 0),
    reservationdate  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

