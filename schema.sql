DROP TABLE IF EXISTS clothes;

CREATE TABLE clothes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price INTEGER NOT NULL,
    description TEXT, 
    image_url TEXT
); 