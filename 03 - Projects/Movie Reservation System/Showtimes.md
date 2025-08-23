```sQL
CREATE TABLE showtimes (
	showtimeid VARCHAR(10) PRIMARY KEY,
	movieid VARCHAR(10) NOT NULL REFERENCES movies(movieid) ON DELETE CASCADE,
	starttime TIMESTAMP NOT NULL,
	endtime TIMESTAMP NOT NULL,
	venue TEXT NOT NULL,
	priceperseat NUMERIC(6,2) NOT NULL,
	availableseats INT NOT NULL CHECK (availableseats >= 0),
	createdat TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	updatedat TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```


```sQL
INSERT INTO showtimes (
  showtimeid, movieid, starttime, endtime, venue, priceperseat, availableseats
) VALUES (
  'st0000001', 'mv001abcd1', '2025-07-28 14:00:00', '2025-07-28 16:30:00', 'Cinema A - Screen 1', 5.50, 100
);

INSERT INTO showtimes (
  showtimeid, movieid, starttime, endtime, venue, priceperseat, availableseats
) VALUES (
  'st0000002', 'mv002efgh2', '2025-07-28 17:00:00', '2025-07-28 18:45:00', 'Cinema B - Screen 3', 4.75, 80
);

INSERT INTO showtimes (
  showtimeid, movieid, starttime, endtime, venue, priceperseat, availableseats
) VALUES (
  'st0000003', '9336f6a5-0', '2025-07-29 13:00:00', '2025-07-29 15:00:00', 'Cinema C - Screen 2', 6.00, 120
);

INSERT INTO showtimes (
  showtimeid, movieid, starttime, endtime, venue, priceperseat, availableseats
) VALUES (
  'st0000004', 'mv001abcd1', '2025-07-29 19:00:00', '2025-07-29 21:30:00', 'Cinema A - Screen 1', 5.50, 90
);

INSERT INTO showtimes (
  showtimeid, movieid, starttime, endtime, venue, priceperseat, availableseats
) VALUES (
  'st0000005', 'mv002efgh2', '2025-07-30 15:30:00', '2025-07-30 17:15:00', 'Cinema D - Screen 4', 4.75, 75
);

```