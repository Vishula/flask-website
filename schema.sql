DROP TABLE IF EXISTS clothes;

CREATE TABLE clothes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price INTEGER NOT NULL,
    description TEXT, 
    image_url TEXT
); 

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    user_password TEXT
);