-- ! INSERT INTO table_name (f1, f2, .., fn) VALUES (v1, v2, .., vn);
--? INSERT INTO departments (id, name) VALUES
--     (00001, 'Production'),
--     (00002, 'Sales'),
--     (00003, 'Buying'),
--     (00004, 'Marketing'),
--     (00005, 'Tech-support');
--? INSERT INTO employees (id, name, rg, gender, department_id, address, city, salary) VALUES
--     (01001, 'Jose da Silva',    20345231, 'M', 00001, 'Rua Campos Filho, 234',    'Itu', 2895.12),
--     (01002, 'Adriana Barros',   23123001, 'F', 00002, 'Av Sampaio Correia, 1234', 'Sorocaba', 15345.01),
--     (01003, 'Ronny Ferreira',   11345123, 'M', 00001, 'Alameda Itororo, 123',     'Sao Paulo', 4234.12),
--     (01004, 'Marecelo Mapiado', 24234678, 'M', 00004, 'Rua Parco Vilela, 321',    'Salto', 23567.00),
--     (01005, 'Luciana Leal',     30234567, 'F', 00003, 'Av Santo Antonio, 12',     'Campinas', 11678.90);
--? INSERT INTO skills(name, field_of_work) VALUES
-- ('Setup production line', 'PRODUCTION'),
-- ('Create Marketing Plan', 'MARKETING'),
-- ('Sale to Mercosul', 'SALES'),
-- ('Production Line maintenance', 'PRODUCTION'),
-- ('Operate CAD and CAM', 'ENGINEERING'),
-- ('Screwing', 'PRODUCTION'),
-- ('Market analysis', 'MARKETING');
INSERT INTO employees_skills(employee_id, skill_id, date) VALUES
(1001, 1, '2022/10/10'),
(1002, 3, '2022/11/20'),
(1003, 1, '2022/03/24'),
-- (2001, 2, '2022/04/27'),
-- (2002, 3, '2022/01/22'),
(1001, 4, '2022/07/15'),
(1003, 4, '2022/11/21');