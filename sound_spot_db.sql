-- Active: 1698513531912@@127.0.0.1@3306
CREATE DATABASE sound_spot
    DEFAULT CHARACTER SET = 'utf8mb4';

USE sound_spot;

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

-- CREATE OR REPLACE TRIGGER