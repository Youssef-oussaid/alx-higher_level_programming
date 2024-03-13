-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
USE hbtn_0c_0;

-- Convert the table's default character set and collation
ALTER TABLE first_table
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Convert the field's character set and collation
ALTER TABLE first_table
    MODIFY COLUMN name VARCHAR(255)
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

