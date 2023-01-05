CREATE TABLE IF NOT EXISTS "skills" (
    "name" varchar(30) NOT NULL,
    "field_of_work" varchar(20) CHECK(
        "field_of_work" in (
            'ENGINEERING',
            'PRODUCTION',
            'MARKETING',
            'SALES',
            'OTHER'
        )
    ),
    "id" INTEGER NOT NULL ,
    PRIMARY KEY ("id" AUTOINCREMENT)
);