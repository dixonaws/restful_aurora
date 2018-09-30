USE employees;
DROP TABLE IF EXISTS employee;

# create the employee table
CREATE TABLE employee (
	id MEDIUMINT AUTO_INCREMENT NOT NULL,
    employeeId varchar(50),
    firstName varchar(50),
    lastName varchar(50),
    phone varchar(50),
    email varchar(50),
    addressLine1 varchar(100),
    addressLine2 varchar(100),
    city varchar(50),
    state varchar(25),
    zipcode varchar(10),
    PRIMARY KEY (id),
    company varchar(50),
    username varchar(50),
    employeeType varchar(50),
    department varchar(50),
    manager varchar(50),
    managerEmail varchar(50),
    mailstop varchar(50)   

);

DELETE FROM employee WHERE id>0;

# load data from a local file (file must have newline characters at the end of each line, choose Excel MS-DOS CSV format)
LOAD DATA LOCAL INFILE 'employees.csv' INTO TABLE employee FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

SELECT * FROM employee;
