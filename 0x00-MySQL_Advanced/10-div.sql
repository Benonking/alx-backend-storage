-- write a fuction to divide two ints if the second numbe is 0 return 0
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC

BEGIN
  RETURN (IF (b = 0,0, a / b));
END //
DELIMITER ;