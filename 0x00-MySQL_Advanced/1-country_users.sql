-- create user table
-- Attributes(id , email, name, country)
CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255),
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
)
