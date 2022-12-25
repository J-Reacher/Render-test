CREATE TABLE Pets (
    name varchar(80),
    pet varchar(80)
   );

INSERT INTO
    Pets
VALUES
    ('Mary', 'dog'),
    ('John', 'cat'),
    ('Robert', 'bird');
    ('Nhat Nam', 'Crocodile'),
    ('Hong Phuc', 'Shark'),
    ('Ngoc Mai', 'Panther'),
    ('Minh Nhan', 'Moew');

CREATE TABLE Students (
    StudentID INT UNSIGNED NOT NULL,
    Name VARCHAR(64),
    Major VARCHAR(32),
    DOB DATE,
    Course YEAR,
    Remaining_fee FLOAT(10),
    In_dormitory ENUM('Yes', 'No'),
    Address VARCHAR(128),
    PRIMARY KEY (StudentID)
);
