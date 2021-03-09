CREATE TABLE users (
    id SERIAL   PRIMARY KEY,
    studentID TEXT  NOT NULL,
    phash TEXT  NOT NULL,
)

CREATE TABLE registers (
    studentID TEXT   NOT NULL,
    courseID TEXT   NOT NULL,
    section INT   NOT NULL,
)