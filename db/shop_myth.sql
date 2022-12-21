DROP TABLE creatures;
DROP TABLE habitats;

CREATE TABLE habitats(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    image VARCHAR(255)
);

CREATE TABLE creatures(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    quantity INT,
    buying_cost FLOAT,
    selling_price FLOAT,
    image VARCHAR (255),
    habitat_id INT NOT NULL REFERENCES habitats(id)
);




 
