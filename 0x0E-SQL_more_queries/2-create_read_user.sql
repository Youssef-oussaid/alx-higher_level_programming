-- create the database hbtn_0d_2 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Use the hbtn_0d_2 database
USE hbtn_0d_2;

-- Create the user user_0d_2 if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to the user user_0d_2 in the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush the privileges to ensure that the changes take effect
FLUSH PRIVILEGES;
