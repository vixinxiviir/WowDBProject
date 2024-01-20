--Achievements Schema
CREATE SCHEMA achievements;


--Achievements Table
CREATE TABLE tbl_achievements(
    achievement_id INT PRIMARY KEY,
    achievement_category_id INT FOREIGN KEY,
    achievement_name VARCHAR(512),
    achievement_description VARCHAR(512),
    achievement_points INT,
    achievement_criteria VARCHAR(512)
);


--Achievement Categories

CREATE TABLE achievements.tbl_achievement_categories(
    achievement_category_id INT PRIMARY KEY,
    achievement_category_name VARCHAR(512),
    achievement_category_parent VARCHAR(512),
    achievement_category_isguild BOOLEAN,
    achievement_cateogory_allquant INT,
    achievement_cateogory_hrdquant INT,
    achievement_cateogory_allpoints INT,
    achievement_cateogory_hrdpoints INT
)