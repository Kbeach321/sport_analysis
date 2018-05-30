
CREATE TABLE epl_data (
    team_name VARCHAR(30),
    wins NUMERIC(2),
    losses NUMERIC(2),
    points NUMERIC(3));

INSERT INTO epl_data VALUES ('Man City', 32, 2, 100);

INSERT INTO epl_data VALUES ('Man United', 25, 7, 81);

INSERT INTO epl_data VALUES ('Tottenham', 23, 7, 77);

INSERT INTO epl_data VALUES ('Liverpool', 21, 5, 75);

INSERT INTO epl_data VALUES ('Chelsea', 21, 10, 70);

INSERT INTO epl_data VALUES ('Arsenal', 19, 13, 63);

INSERT INTO epl_data VALUES ('Burnley FC', 14, 12, 54);

INSERT INTO epl_data VALUES ('Everton', 13, 15, 49);

INSERT INTO epl_data VALUES ('Leicester City', 12, 15, 47);

INSERT INTO epl_data VALUES ('Newcastle', 12, 18, 44);

INSERT INTO epl_data VALUES ('Crystal Palace', 11, 16, 44);

INSERT INTO epl_data VALUES ('Bournemouth', 11, 16, 44);

INSERT INTO epl_data VALUES ('West Ham', 10, 16, 42);

rows = db.query("SELECT * FROM epl_data;")
for row in rows:
    print(row)
