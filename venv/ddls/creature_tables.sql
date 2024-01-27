CREATE SCHEMA creatures;

CREATE TABLE creatures.tbl_creature(
    creature_id INT PRIMARY KEY,
    creature_name VARCHAR(512),
    creature_type_id INT REFERENCES creature.tbl_creature_type(type_id),
    creature_family_id INT REFERENCES creatures.tbl_creature_family(family_id),
    creature_tameable BOOLEAN
);

CREATE TABLE creatures.tbl_creature_family(
    family_id INT PRIMARY KEY,
    specialization VARCHAR(25)
)

CREATE TABLE creatures.tbl_creature_type(
    type_id INT PRIMARY KEY,
    type_name VARCHAR(512)
)