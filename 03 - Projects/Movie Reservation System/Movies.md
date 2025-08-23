## SQL table
```sQL
CREATE TABLE movies (
	movieid VARCHAR(10) PRIMARY KEY,
	title TEXT NOT NULL,
	description TEXT,
	genre TEXT NOT NULL,
	duration INT NOT NULL, -- in minutes
	director TEXT NOT NULL,
	posterimage Text NOT NULL,
	releasedate TIMESTAMP NOT NULL,
	createdat TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	updatedat TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
)
```

```sQL
INSERT INTO movies (movieid, title, description, genre, duration, director, posterimage, releasedate)
VALUES (
  'mv001abcd1',
  'Inception',
  'A skilled thief who steals corporate secrets through dream-sharing technology is given a chance at redemption.',
  'Sci-Fi',
  148,
  'Christopher Nolan',
  'https://example.com/posters/inception.jpg',
  '2010-07-16 00:00:00'
);

INSERT INTO movies (movieid, title, description, genre, duration, director, posterimage, releasedate)
VALUES (
  'mv002efgh2',
  'The Grand Budapest Hotel',
  'A concierge and his protégé become entangled in a murder mystery involving a priceless painting and a wealthy family.',
  'Comedy',
  99,
  'Wes Anderson',
  'https://example.com/posters/grandbudapest.jpg',
  '2014-03-28 00:00:00'
);

INSERT INTO movies (movieid, title, description, genre, duration, director, posterimage, releasedate)
VALUES (
  'mv003ijkl3',
  'Parasite',
  'A poor family schemes to become employed by a wealthy family by infiltrating their household.',
  'Thriller',
  132,
  'Bong Joon-ho',
  'https://example.com/posters/parasite.jpg',
  '2019-05-30 00:00:00'
);

INSERT INTO movies (movieid, title, description, genre, duration, director, posterimage, releasedate)
VALUES (
  'mv004mnop4',
  'The Matrix',
  'A computer hacker learns the true nature of his reality and joins a rebellion against its controllers.',
  'Action',
  136,
  'Lana Wachowski, Lilly Wachowski',
  'https://example.com/posters/matrix.jpg',
  '1999-03-31 00:00:00'
);

INSERT INTO movies (movieid, title, description, genre, duration, director, posterimage, releasedate)
VALUES (
  'mv005qrst5',
  'Spirited Away',
  'A ten-year-old girl enters a world of spirits and must find a way to free herself and her parents.',
  'Animation',
  125,
  'Hayao Miyazaki',
  'https://example.com/posters/spiritedaway.jpg',
  '2001-07-20 00:00:00'
);

```