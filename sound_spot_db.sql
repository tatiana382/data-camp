-- Active: 1698594207995@@127.0.0.1@3306@sound_spot
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
    track_id                          VARCHAR(50)        NOT NULL,
    main_artist_id                    VARCHAR(50)        NOT NULL,
    released_date                     DATE               NOT NULL,
    loudness                          DECIMAL(8, 4),
    tempo                             DECIMAL(8, 4),
    tempo_confidence                  DECIMAL(8, 4),
    time_signature                    DECIMAL(8, 4),
    time_signature_confidence         DECIMAL(8, 4),
    track_name                        VARCHAR(100)       NOT NULL,
    track_popularity                  INT(3)             NOT NULL,
    other_artists                     VARCHAR(100),
    track_image_url                   TEXT,
    lyrics                            TEXT,
    PRIMARY KEY (track_id),
    FOREIGN KEY (main_artist_id) REFERENCES MAIN_ARTIST(main_artist_id)
);

SHOW TABLES;

SELECT @@hostname;

SELECT * FROM track;

DROP DATABASE sound_spot;
