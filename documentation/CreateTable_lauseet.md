CREATE TABLE Team (
    id integer PRIMARY KEY,
    date_created datetime,
    date_modified datetime,
    name varchar(144),
    home varchar(144)
);

CREATE TABLE Account (
    id integer PRIMARY KEY,
    date_created datetime,
    date_modified datetime,
    name varchar(144),
    username varchar(144),
    password varchar(144),
    isAdmin boolean
);

CREATE TABLE Cup (
    id integer PRIMARY KEY,
    date_created datetime,
    date_modified datetime,
    account_id integer,
    name varchar(144),
    start_time datetime,
    end_time datetime,
    points integer,
    FOREIGN KEY (account_id) REFERENCES Account(id)
);

CREATE TABLE Result (
    id integer PRIMARY KEY,
    date_created datetime,
    date_modified datetime,
    team_id integer,
    cup_id integer,
    rank integer,
    points integer,
    FOREIGN KEY (team_id) REFERENCES Team(id),
    FOREIGN KEY (cup_id) REFERENCES Cup(id)
)