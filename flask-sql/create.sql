CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Denpasar', 4150);
INSERT INTO flights (origin, destination, duration) VALUES ('Cilacap', 'London', 2314);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Jakarta', 666);
INSERT INTO flights (origin, destination, duration) VALUES ('Cilacap', 'London', 987);
INSERT INTO flights (origin, destination, duration) VALUES ('Malang', 'Jakarta', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Jakarta', 231);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Cilacap', 'Denpasar', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Malang', 'London', 111);

UPDATE flights SET duration = 4512 WHERE destination = 'Denpasar' AND origin = 'New York';


CREATE TABLE passengers (
   id SERIAL PRIMARY KEY, 
   name VARCHAR NOT NULL,
   flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers (name, flight_id) VALUES ('Alice',1);
INSERT INTO passengers (name, flight_id) VALUES ('Rozak',1);
INSERT INTO passengers (name, flight_id) VALUES ('Abdul',2);
INSERT INTO passengers (name, flight_id) VALUES ('Paimin',2);
INSERT INTO passengers (name, flight_id) VALUES ('Sukino',4);
INSERT INTO passengers (name, flight_id) VALUES ('Tuminem',9);
INSERT INTO passengers (name, flight_id) VALUES ('Kemud',9);


