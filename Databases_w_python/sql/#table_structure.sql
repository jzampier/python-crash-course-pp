CREATE TABLE IF NOT EXISTS table_name (
    -- !Starts with Foreign Key "tableWhereTheForeignKeyIsComming_id"
    table_where_FK_is_id INTEGER REFERENCES table_name (id),
    field_1,
    .
    .
    .
    field_n,
    date date,
    -- !Ends with Primary Key just "id"
    id SERIAL PRIMARY KEY
);