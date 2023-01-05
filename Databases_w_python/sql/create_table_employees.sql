CREATE TABLE employees(
	"department_id" decimal(5),
	"name"       char(30) NOT NULL,
	"rg"         decimal(9) NOT NULL UNIQUE,
	"gender"     char(1) CHECK(gender in ('M', 'F')),
	"address"    varchar(50),
	"city"       varchar(20) DEFAULT 'Sao Paulo',
	"salary"     decimal(10,2),
	"id"   decimal(5) NOT NULL,
	PRIMARY KEY  (id),
	FOREIGN KEY  (department_id) REFERENCES departments(id)
)