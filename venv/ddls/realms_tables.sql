--Realms Schema
CREATE SCHEMA realms;

--Realm Table
CREATE TABLE realms.tbl_realm (
    realm_id INT PRIMARY KEY,
    realm_name VARCHAR(512),
    realm_region VARCHAR(512),
    realm_queue VARCHAR(512),
    realm_status VARCHAR(512),
    realm_population INT
);

--Connected Realm (child realm) Table
CREATE TABLE realms.tbl_realm_conn(
    conn_realm_id INT PRIMARY KEY,
    conn_realm_name VARCHAR(512),
    conn_realm_parent INT REFERENCES realms.tbl_realm(realm_id),
    conn_realm_cat VARCHAR(512),
    conn_realm_locale VARCHAR(512),
    conn_realm_timezone VARCHAR(512),
    conn_realm_type VARCHAR(512),
    conn_realm_tourney BOOLEAN
);

--Realm Auction Table
CREATE TABLE realms.tbl_auction(
    auction_id INT PRIMARY KEY,
    auction_realm INT REFERENCES realms.tbl_realm(realm_id),
    auction_item INT,
    auction_quant INT,
    auction_type INT,
    auction_value INT,
    auction_buyout INT,
    auction_timeleft VARCHAR(512)
);
