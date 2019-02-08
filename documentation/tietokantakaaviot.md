CREATE TABLE Joukkue (
    id integer PRIMARY KEY,
    date_created date,
    date_modified date,
    name varchar(144),
    home varchar(144)
);

CREATE TABLE Account (
    id integer PRIMARY KEY,
    date_created date,
    date_modified date,
    name varchar(144),
    username varchar(144),
    password varchar(144)
);

CREATE TABLE Cup (
    id integer PRIMARY KEY,
    date_created date,
    date_modified date,
    name varchar(144),
    start_time varchar(144),
    end_time varchar(144),
    points integer
);

CREATE TABLE Result (
    id integer PRIMARY KEY,
    date_created date,
    date_modified date,
    joukkue_id integer,
    cup_id integer,
    rank integer,
    points integer,
    FOREIGN KEY (joukkue_id) REFERENCES Joukkue(id),
    FOREIGN KEY (cup_id) REFERENCES Cup(id)
)