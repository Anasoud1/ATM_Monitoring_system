DROP DATABASE IF EXISTS atm_db;
CREATE DATABASE IF NOT EXISTS atm_db;
CREATE USER IF NOT EXISTS 'atm_user'@'localhost' IDENTIFIED BY 'atm_pwd';
GRANT SELECT ON `performance_schema`.* TO 'atm_user'@'localhost';
FLUSH PRIVILEGES;
