-- create trigger that resets  the atrribute "valid_email" 
-- only if the email has been changed
-- distribute the logic to all databases
DELIMITER // ;
CREATE TRIGGER resets_validate_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email != OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END;
DELIMITER ;

