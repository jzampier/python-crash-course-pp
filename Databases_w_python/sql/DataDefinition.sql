--! DROP TABLE IF EXISTS table_name;

--? Including fields
--? ALTER TABLE table_name(
--? add cic decimal(11) NOT NULL UNIQUE,
--? add noth decimal(5)
--? );

--? Remove fields
--? ALTER TABLE table_name(
--? drop noth
--? );

--? Changing fields (var type)
--? ALTER TABLE table_name(
--? alter cic type varchar(10) NOT NULL UNIQUE
--? );

--? Changing fields (field names)
--? ALTER TABLE table_name(
--? alter cic to cpf
--? );