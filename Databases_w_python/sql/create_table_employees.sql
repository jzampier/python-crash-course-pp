CREATE TABLE employees(
	"register"   decimal(5) NOT NULL,
	"name"       char(30) NOT NULL,
	"rg"         decimal(9) NOT NULL UNIQUE,
	"gender"     char(1) CHECK(gender in ('M', 'F')),
	"department" decimal(5),
	"address"    varchar(50),
	"city"       varchar(20) DEFAULT 'Sao Paulo',
	"salary"     decimal(10,2),
	PRIMARY KEY  (register),
	FOREIGN KEY  (department) REFERENCES departments(department_id)
)