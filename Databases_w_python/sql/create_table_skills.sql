CREATE TABLE IF NOT EXISTS "skills" (
    "skill_id" INTEGER NOT NULL ,
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
    PRIMARY KEY ("skill_id" AUTOINCREMENT)
);