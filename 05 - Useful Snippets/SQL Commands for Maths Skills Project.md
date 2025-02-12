```SQL
%%Chats%%
CREATE TABLE chats ( id SERIAL PRIMARY KEY, userid VARCHAR(8) NOT NULL REFERENCES users(userId), chatid VARCHAR(8) NOT NULL UNIQUE, chat JSON, chatname TEXT );
```

```SQL
%%Years%%
CREATE TABLE years ( id SERIAL PRIMARY KEY, name TEXT NOT NULL UNIQUE, description TEXT NOT NULL );


INSERT INTO years (name, description)
VALUES
    ('KG', 'Kindergarten'),
    ('Year 1', 'First year of primary education'),
    ('Year 2', 'Second year of primary education'),
    ('Year 3', 'Third year of primary education'),
    ('Year 4', 'Fourth year of primary education'),
    ('Year 5', 'Fifth year of primary education'),[[Tasks]]
    ('Year 6', 'Sixth year of primary education'),
    ('Year 7', 'Seventh year of primary education'),
    ('Year 8', 'Eighth year of primary education');
```

```SQL
%%Session Scores%%
CREATE TABLE sessionScores (
	id SERIAL PRIMARY KEY,
	userId VARCHAR(8) NOT NULL REFERENCES users(userId),
	skills JSONB NOT NULL, 
	answeredQuestions JSONB NOT NULL, 
	score INT NOT NULL, 
	sessionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);
```

```SQL
%%Skills%%
CREATE TABLE skills(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL UNIQUE,
	description TEXT,
	pictureLink VARCHAR(2083),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO skills (name, description)
VALUES
    ('Integration', 'The process of finding the integral of a function.'),
    ('Differentiation', 'The process of finding the derivative of a function.'),
    ('Algebra', 'The branch of mathematics dealing with symbols and the rules for manipulating those symbols.'),
    ('Geometry', 'The branch of mathematics concerned with the properties and relations of points, lines, surfaces, and solids.'),
    ('Discrete Mathematics', 'The study of mathematical structures that are fundamentally discrete rather than continuous.');
```

```SQL
# Questions
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    skillId INT REFERENCES skills(id),
    skill TEXT NOT NULL,
    questionLatex TEXT NOT NULL,
    questionType TEXT NOT NULL CHECK (questionType IN ('True/False', 'MCQ')),
    correctAnswer TEXT NOT NULL,
    incorrectAnswers JSONB NOT NULL,
    addedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    addedBy VARCHAR(8) NOT NULL,
    difficulty TEXT NOT NULL CHECK (difficulty IN ('easy', 'medium', 'hard')) DEFAULT 'easy'
);


INSERT INTO questions (skillId, skill, questionLatex, questionType, correctAnswer, incorrectAnswers, addedBy, difficulty)
VALUES
(1, 'Integration', '$\\int x^2 dx$', 'MCQ', '$\\frac{1}{3}x^3 + C$', '["$\\frac{1}{2}x^2 + C$", "$2x + C$", "$\\frac{1}{4}x^4 + C$"]', 'AO000001', 'easy'),

(1, 'Integration', '$\\int \\sin(x) dx$', 'MCQ', '$-\\cos(x) + C$', '["$\\sin(x) + C$", "$\\frac{1}{\\sin(x)} + C$", "$\\frac{x}{\\cos(x)} + C$"]', 'AO000001', 'medium'),

(1, 'Integration', '$\\int \\frac{1}{x} dx$', 'MCQ', '$\\ln|x| + C$', '["$x\\ln(x) + C$", "$\\frac{1}{2}x^2 + C$", "$e^x + C$"]', 'AO000001', 'hard'),

(1, 'Integration', '$\\int e^x dx = e^x + C$', 'True/False', 'True', '["False"]', 'AO000001', 'easy'),

(1, 'Integration', '$\\int \\cos(x) dx$', 'MCQ', '$\\sin(x) + C$', '["$-\\sin(x) + C$", "$x\\cos(x) + C$", "$\\tan(x) + C$"]', 'AO000001', 'medium'),

(2, 'Differentiation', '$\\frac{d}{dx}x^3$', 'MCQ', '$3x^2$', '["$x^3$", "$3x$", "$2x^2$"]', 'AO000001', 'hard'),

(2, 'Differentiation', '$\\frac{d}{dx}\\sin(x)$', 'MCQ', '$\\cos(x)$', '["$-\\sin(x)$", "$\\frac{1}{\\sin(x)}$", "$\\tan(x)$"]', 'AO000001', 'easy'),

(2, 'Differentiation', '$\\frac{d}{dx}\\ln(x)$', 'MCQ', '$\\frac{1}{x}$', '["$\\frac{x}{\\ln(x)}$", "$\\ln(x) + 1$", "$\\frac{1}{x^2}$"]', 'AO000001', 'medium'),

(2, 'Differentiation', '$\\frac{d}{dx}(e^x) = e^x$', 'True/False', 'True', '["False"]', 'AO000001', 'hard'),

(2, 'Differentiation', '$\\frac{d}{dx}(x^2 + 2x + 1)$', 'MCQ', '$2x + 2$', '["$x + 2$", "$2x + 1$", "$3x^2$"]', 'AO000001', 'easy'),

(3, 'Algebra', '$Solve\\ for\\ x:\\ 2x + 3 = 7$', 'MCQ', '$2$', '["$1$", "$3$", "$4$"]', 'AO000001', 'medium'),

(3, 'Algebra', '$Is\\ the\\ equation\\ x^2 + 2x + 1 = 0\\ a\\ quadratic\\ equation?$', 'True/False', 'True', '["False"]', 'AO000001', 'hard'),

(3, 'Algebra', '$Factorize\\ the\\ expression\\ x^2 - 5x + 6$', 'MCQ', '$(x-2)(x-3)$', '["$(x+2)(x+3)$", "$(x-1)(x-6)$", "$(x+1)(x+6)$"]', 'AO000001', 'easy'),

(3, 'Algebra', '$The\\ product\\ of\\ any\\ two\\ real\\ numbers\\ is\\ always\\ a\\ real\\ number.$', 'True/False', 'True', '["False"]', 'AO000001', 'medium'),

(3, 'Algebra', '$Simplify\\ the\\ expression:\\ (2x + 3)(x - 1)$', 'MCQ', '$2x^2 + x - 3$', '["$2x^2 - x - 3$", "$2x^2 + 5x + 3$", "$x^2 + x - 1$"]', 'AO000001', 'hard'),

(4, 'Geometry', '$The\\ sum\\ of\\ the\\ angles\\ in\\ a\\ triangle\\ is\\ 180\\ degrees.$', 'True/False', 'True', '["False"]', 'AO000001', 'easy'),

(4, 'Geometry', '$Is\\ a\\ square\\ a\\ type\\ of\\ rectangle?$', 'True/False', 'True', '["False"]', 'AO000001', 'medium'),

(4, 'Geometry', '$Calculate\\ the\\ area\\ of\\ a\\ circle\\ with\\ radius\\ 5.$', 'MCQ', '$25\\pi$', '["$20\\pi$", "$30\\pi$", "$50\\pi$"]', 'AO000001', 'hard'),

(4, 'Geometry', '$Which\\ of\\ the\\ following\\ is\\ a\\ property\\ of\\ all\\ parallelograms?$', 'MCQ', '$Opposite\\ sides\\ are\\ equal$', '["$All\\ angles\\ are\\ right\\ angles$", "$Diagonals\\ are\\ equal$", "$Opposite\\ angles\\ are\\ complementary$"]', 'AO000001', 'easy'),

(4, 'Geometry', '$The\\ diagonals\\ of\\ a\\ rhombus\\ are\\ perpendicular.$', 'True/False', 'True', '["False"]', 'AO000001', 'medium'),

(5, 'Discrete Mathematics', '$In\\ a\\ set,\\ order\\ of\\ elements\\ does\\ not\\ matter.$', 'True/False', 'True', '["False"]', 'AO000001', 'hard'),

(5, 'Discrete Mathematics', '$The\\ sum\\ of\\ the\\ first\\ n\\ natural\\ numbers\\ is\\ \\frac{n(n+1)}{2}$', 'True/False', 'True', '["False"]', 'AO000001', 'easy'),

(5, 'Discrete Mathematics', '$What\\ is\\ the\\ number\\ of\\ subsets\\ of\\ a\\ set\\ with\\ 3\\ elements?$', 'MCQ', '$8$', '["$6$", "$4$", "$7$"]', 'AO000001', 'medium'),

(5, 'Discrete Mathematics', '$In\\ graph\\ theory,\\ a\\ tree\\ is\\ a\\ connected\\ graph\\ with\\ no\\ cycles.$', 'True/False', 'True', '["False"]', 'AO000001', 'hard'),

(5, 'Discrete Mathematics', '$How\\ many\\ edges\\ does\\ a\\ complete\\ graph\\ with\\ 4\\ vertices\\ have?$', 'MCQ', '$6$', '["$4$", "$8$", "$10$"]', 'AO000001', 'easy');
```

```SQL
%%Users%%
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fname VARCHAR(255) NOT NULL,
    lname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    userId VARCHAR(8) NOT NULL UNIQUE,
    userRole VARCHAR(10) CHECK (userRole IN ('admin', 'student')),
    plan VARCHAR(10) NOT NULL DEFAULT 'bronze' CHECK (
        (userRole = 'admin' AND plan = 'all-access') OR
        (userRole = 'student' AND plan IN ('bronze', 'silver', 'gold'))
    )
);
```

