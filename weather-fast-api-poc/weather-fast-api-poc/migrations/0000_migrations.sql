CREATE TABLE IF NOT EXISTS "migrations" (
    "filename" VARCHAR(255) PRIMARY KEY NOT NULL,
    "migration_date" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);