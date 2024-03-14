REATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user exists before creating it
SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost';

-- If the user doesn't exist, create it
IF @user_exists = 0 THEN
	    CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
END IF;

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

