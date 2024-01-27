CREATE SCHEMA items;


CREATE TABLE items.tbl_item(
    item_id INT PRIMARY KEY,
    item_name VARCHAR(512),
    item_quality VARCHAR(512),
    item_level INT,
    item_required_level INT,
    item_class_id INT REFERENCES items.tbl_item_class(class_id),
    item_subclass_id INT REFERENCES item.tbl_item_subclass(subclass_id),
    item_purchase_price INT,
    item_sell_price INT,
    item_equippable BOOLEAN,
    item_stackable BOOLEAN
);

CREATE TABLE items.tbl_item_class(
    class_id INT PRIMARY KEY,
    class_name VARCHAR(512)
);

CREATE TABLE items.tbl_item_subclass(
    subclass_id INT PRIMARY KEY,
    subclass_name VARCHAR(512),
    subclass_parent INT REFERENCES items.tbl_item_class(class_id)
);