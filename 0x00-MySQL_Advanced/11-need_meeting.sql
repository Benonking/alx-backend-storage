-- create a view need_meeting that lists all students that have under 80(strict)
-- and no last meeting for more than 1 month

CREATE VIEW need_meeting 
SELECT name from student
WHERE score < 80 AND (students.last_meeting is NULL 0R student.last_meeting < DATE_ADD(NOW(), INTERVAL -1 MONTH));
DELIMITER ;