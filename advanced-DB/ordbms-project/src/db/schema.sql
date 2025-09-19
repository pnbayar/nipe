CREATE TABLE dim_platform (
    platform_id SERIAL PRIMARY KEY,
    name TEXT,
    category TEXT,
    metadata JSONB
);

CREATE TABLE dim_user (
    user_id SERIAL PRIMARY KEY,
    username TEXT,
    age INT,
    country TEXT
);

CREATE TABLE dim_date (
    date_id SERIAL PRIMARY KEY,
    full_date DATE,
    day INT,
    month INT,
    year INT
);

CREATE TABLE dim_content (
    content_id SERIAL PRIMARY KEY,
    title TEXT,
    content_type TEXT,
    tags TEXT[],
    media_info JSONB
);

CREATE TABLE fact_engagement (
    engagement_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES dim_user(user_id),
    content_id INT REFERENCES dim_content(content_id),
    platform_id INT REFERENCES dim_platform(platform_id),
    date_id INT REFERENCES dim_date(date_id),
    watch_time INT,
    rating NUMERIC(2,1),
    interaction JSONB
);