-- creates the database hbtn_0d_2 and the user user_0d_2

CREATE DATABASE IF NOT EXISTS hbtn;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user0d_2_pwd';
GRANT SELECT ON hbtn TO 'user_0d_2'@'localhost';