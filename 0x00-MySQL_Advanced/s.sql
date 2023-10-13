SELECT users.name corrections.score
FROM users 
LEFT JOIN ON users.id = corrections.user_id;