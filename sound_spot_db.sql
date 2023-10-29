-- Active: 1698594207995@@127.0.0.1@3306@sound_spot
-- CREATE DATABASE sound_spot
--     DEFAULT CHARACTER SET = 'utf8mb4';

-- USE sound_spot;

-- SHOW TABLES;

CREATE TABLE IF NOT EXISTS MAIN_ARTIST
(
    main_artist_id             VARCHAR(50)        NOT NULL,
    main_artist_name           VARCHAR(100)       NOT NULL,
    main_artist_popularity     INT(3)             NOT NULL,
    main_artist_genre          VARCHAR(100)       NOT NULL,
    main_artist_image_url      TEXT,
    PRIMARY KEY (main_artist_id)
);

CREATE TABLE IF NOT EXISTS TRACK
(
    track_id            VARCHAR(50)        NOT NULL,
    main_artist_id      VARCHAR(50)        NOT NULL,
    released_date       DATE               NOT NULL,
    track_name          VARCHAR(100)       NOT NULL,
    track_popularity    INT(3)             NOT NULL,
    other_artists       VARCHAR(100),
    track_image_url     TEXT,
    lyrics              TEXT,
    PRIMARY KEY (track_id),
    FOREIGN KEY (main_artist_id) REFERENCES MAIN_ARTIST(main_artist_id)
);

DELIMITER //
-- Trigger to avoid duplicate tracks
CREATE TRIGGER check_existing_track
BEFORE INSERT ON TRACK
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM TRACK WHERE track_id = NEW.track_id) OR
       EXISTS (SELECT 1 FROM TRACK WHERE main_artist_id = NEW.main_artist_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'This track or main artist already exists in the database!';
    END IF;
END;
//

-- Trigger to avoid duplicate artists
CREATE TRIGGER check_existing_main_artist
BEFORE INSERT ON MAIN_ARTIST
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM MAIN_ARTIST WHERE main_artist_id = NEW.main_artist_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'This artist already exists in the database!';
    END IF;
END;
//
DELIMITER ;

SHOW TRIGGERS;

-- SELECT * FROM track;